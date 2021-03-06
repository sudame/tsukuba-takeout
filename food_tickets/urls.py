from django.urls import path
from . import views

app_name = "food_tickets"
urlpatterns = [
    path("", views.StoreListView.as_view(), name="index"),
    path("store/<int:pk>", views.StoreView.as_view(), name="store"),
    path("ticket/<int:pk>/buy", views.TicketBuyView.as_view(), name="ticket_buy"),
    path("ticket/<int:pk>", views.TicketDetailView.as_view(), name="ticket_detail"),
]
