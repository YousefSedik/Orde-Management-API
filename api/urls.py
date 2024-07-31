from django.urls import path
from . import views


urlpatterns = [
    path(
        "cart",
        views.ListCreateCartAPIView.as_view(),
        name="list-create-cart",
    ),
    path(
        "cart/<int:pk>",
        views.UpdateDeleteCartAPIView.as_view(),
        name="update-delete-cart",
    ),
    path(
        "order",
        views.CreateOrderAPIView.as_view(),
        name="create-order",
    ),
    path("orders", views.ListOrdersAPIView.as_view(), name="list-order"),
    path(
        "order-details/<int:pk>",
        views.RetrieveOrderDetailsAPIView.as_view(),
        name="retrieve-order-details",
    ),
    path(
        "order/<int:pk>",
        views.UpdateRetrieveOrderAPIView.as_view(),
        name="retrieve-update-order",
    ),
]
