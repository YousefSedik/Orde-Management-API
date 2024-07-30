from rest_framework.serializers import ModelSerializer
from core.models import Product, Cart, Order, OrderItem


class CartCreateSerializer(ModelSerializer):

    def save(self, *args, **kwargs):
        self.user = self.context["request"].user
        return super().save(*args, **kwargs)

    class Meta:
        model = Cart
        fields = ["id", "user", "product", "quantity"]


class CartListSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "product", "quantity"]


class CartUpdateSerializer(ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ["id", "quantity"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock"]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "user", "orderDate", "status"]


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["product", "order", "quantity"]
