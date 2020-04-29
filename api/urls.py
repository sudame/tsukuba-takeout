from .views import StoreListAPIView
from django.urls import path, include

urlpatterns = [
    path("store/list", StoreListAPIView.as_view(), name="store_list_api"),
]
