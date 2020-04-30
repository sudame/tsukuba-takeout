from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Store, Ticket
from django.template import loader
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from api.serializers import StoreSerializer
import json
import payjp
import os

payjp.api_key = os.getenv("PAYJP_SECRET_KEY")


class StoreListView(generic.ListView):
    model = Store
    template_name = "food_tickets/storeList.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(kwargs)
        data["store_list_object"] = json.dumps(
            StoreSerializer(Store.objects.all(), many=True).data, ensure_ascii=False
        )
        return data


class StoreView(LoginRequiredMixin, generic.DetailView):
    model = Store
    template_name = "food_tickets/store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class TicketDetailView(generic.DetailView):
    model = Ticket


class TicketBuyView(generic.DetailView, LoginRequiredMixin):
    model = Ticket
    template_name = "food_tickets/ticket_buy.html"

    def post(self, request: HttpRequest, *args, **kwargs):
        payjp_token = request.POST["payjp-token"]
        charge = payjp.Charge.create(amount=300, card=payjp_token, currency="jpy",)
        return HttpResponse(json.dumps(charge), content_type="application/json")
