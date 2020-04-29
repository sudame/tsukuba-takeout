from django.shortcuts import render
from rest_framework import generics
from .serializers import StoreSerializer
from food_tickets.models import Store


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
