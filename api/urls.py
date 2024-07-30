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
]
