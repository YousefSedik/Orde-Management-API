from rest_framework.serializers import ModelSerializer
from core.models import Product, Cart, Order, OrderItem


class ListCreateCartSerializer(ModelSerializer):

    def save(self, **kwargs):
        self.validated_data["user"] = self.context["request"].user
        return super().save(**kwargs)

    class Meta:
        model = Cart
        fields = ["id", "product", "quantity"]


class UpdateDestroyCartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ["id", "product", "quantity"]
