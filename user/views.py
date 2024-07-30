from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token


# Create your views here.


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
