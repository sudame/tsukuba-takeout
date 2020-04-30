from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Store, Ticket
from django.template import loader
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from api.serializers import StoreSerializer
import json
import payjp
from payjp.error import PayjpException
import os
from .forms import PaymentForm

payjp.api_key = os.getenv("PAYJP_SECRET_KEY")


class StoreListView(generic.ListView):
    model = Store
    template_name = "food_tickets/storeList.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["store_list_object"] = json.dumps(
            StoreSerializer(Store.objects.all(), many=True).data, ensure_ascii=False
        )
        return data


class StoreView(generic.DetailView):
    model = Store
    template_name = "food_tickets/store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(kwargs=kwargs)
        context["user"] = self.request.user
        return context


class TicketDetailView(generic.DetailView):
    model = Ticket


class TicketBuyView(LoginRequiredMixin, generic.DetailView):
    model = Ticket
    template_name = "food_tickets/ticket_buy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(kwargs=kwargs)
        context["payjp_public_key"] = os.getenv("PAYJP_PUBLIC_KEY")
        return context

    # TODO: NEED refactoring!!!!!!!!!!!!!!!!!
    def post(self, request: HttpRequest, *args, **kwargs):
        form = PaymentForm(request.POST)
        if form.is_valid():
            self.object = self.get_object()
            ticket: Ticket = super(TicketBuyView, self).get_context_data()["ticket"]
            try:
                charge = payjp.Charge.create(
                    amount=ticket.price,
                    card=form.cleaned_data["payjp_token"],
                    currency="jpy",
                )
            except PayjpException as payjp_err:
                return HttpResponse("error: {0}".format(payjp_err))
            return HttpResponse(json.dumps(charge), content_type="application/json")
        else:
            return HttpResponse("error.")
