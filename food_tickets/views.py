from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Store
from django.template import loader
from django.views import generic


class IndexView(generic.ListView):
    model = Store
    template_name = "food_tickets/storeList.djt"


class StoreView(generic.DetailView):
    model = Store
    template_name = "food_tickets/store.djt"
