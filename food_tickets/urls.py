from django.urls import path
from . import views

app_name = "food_tickets"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("store/<int:pk>", views.StoreView.as_view(), name="store"),
]
