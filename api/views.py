# from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from api import serializers
from rest_framework.response import Response
from core.models import Cart, Order, OrderItem
from rest_framework import status
from rest_framework import serializers as rest_serializers

# import generic views

from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    GenericAPIView,
    ListCreateAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated


class ListCreateCartAPIView(ListCreateAPIView):
    serializer_class = serializers.ListCreateCartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "Product already exists in cart"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)


class UpdateDeleteCartAPIView(GenericAPIView, DestroyModelMixin, UpdateModelMixin):
    serializer_class = serializers.UpdateDestroyCartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CreateOrderAPIView(CreateAPIView):
    serializer_class = serializers.CreateOrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except rest_serializers.ValidationError as e:
            return Response(
                {"error": f"Transaction failed: {e.detail}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": f"Transaction failed: {e.detail}"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ListOrdersAPIView(ListAPIView):
    serializer_class = serializers.RetrieveListOrderSerializer
    queryset = Order.objects.all()


class RetrieveOrderDetailsAPIView(RetrieveAPIView):
    serializer_class = serializers.RetrieveListOrderSerializer
    queryset = Order.objects.all()


class RetrieveOrderAPIView(RetrieveAPIView):
    serializer_class = serializers.RetrieveOrderSerializer
    queryset = Order.objects.all()
