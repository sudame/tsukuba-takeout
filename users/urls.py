from django.urls import path, include
from .views import SignUpView

# app_name = "users"
urlpatterns = [
    path("", include("allauth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
]
