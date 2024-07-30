from .views import CustomObtainAuthToken
from django.urls import path

urlpatterns = [
    path("api-token-auth/", CustomObtainAuthToken.as_view()),
]
