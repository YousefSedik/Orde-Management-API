from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Product, Cart, Order, OrderItem
from django.db import transaction


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


# create a transaction


class CreateOrderSerializer(ModelSerializer):
    def create(self, validated_data):
        self.validated_data["user"] = self.context["request"].user
        try:
            with transaction.atomic():
                order = Order.objects.create(user=self.validated_data["user"])
                cart_objs = Cart.objects.filter(
                    user=self.validated_data["user"]
                ).select_related("product")
                if not cart_objs.exists():
                    raise serializers.ValidationError("Cart is empty")

                total_price = 0
                for obj in cart_objs:
                    order_item = OrderItem.objects.create(
                        product=obj.product,
                        order=order,
                        quantity=obj.quantity,
                        price=obj.product.price,
                    )
                    if obj.quantity > obj.product.stock:
                        raise serializers.ValidationError(
                            f"Only {obj.product.stock} items left in stock"
                        )
                    obj.product.stock -= obj.quantity
                    obj.product.save()
                    total_price += order_item.price * order_item.quantity

                order.total_price = total_price
                cart_objs.delete()
                order.save()

        except serializers.ValidationError:
            raise

        except Exception:
            raise
        return order

    class Meta:
        model = Order
        fields = ["id", "orderDate", "status"]


class OrderItemsInlineSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price"]


class RetrieveListOrderSerializer(ModelSerializer):
    order_items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "orderDate",
            "status",
            "order_items",
            "total_price",
            "last_updated",
        ]

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        return OrderItemsInlineSerializer(order_items, many=True).data


class RetrieveOrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ["id", "orderDate", "status", "total_price", "last_updated"]


class UpdateOrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "status"]
