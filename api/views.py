# from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from api import serializers
from rest_framework.response import Response
from core.models import Cart, Order, OrderItem
from rest_framework import status

# import generic views

from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    GenericAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class GetCartAPIView(ListAPIView):
    serializer_class = serializers.CartListSerializer
    queryset = Cart.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)


class CreateCartAPIView(CreateAPIView):
    serializer_class = serializers.CartCreateSerializer
    queryset = Cart.objects.all()
