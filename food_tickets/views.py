from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Store
from django.template import loader
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class StoreListView(generic.ListView):
    model = Store
    template_name = "food_tickets/storeList.html"


class StoreView(LoginRequiredMixin, generic.DetailView):
    model = Store
    template_name = "food_tickets/store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
