from django.urls import path, include
from allauth.account.views import SignupView, LoginView, LogoutView

# app_name = "users"
urlpatterns = [
    path("signin/", LoginView.as_view(), name="account_login"),
    path("signup/", SignupView.as_view(), name="account_signup"),
    path("signout/", LogoutView.as_view(), name="account_logout"),
]
