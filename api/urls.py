from django.urls import path
from . import views


urlpatterns = [
    path("cart", views.GetCartAPIView.as_view(), name="get-cart"),
    path("cart", views.CreateCartAPIView.as_view(), name="create-cart"),
]
