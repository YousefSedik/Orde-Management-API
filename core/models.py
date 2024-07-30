from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    class ORDER_STATUS(models.TextChoices):
        PENDING = "1", "Pending"
        CANCELED = "2", "Canceled"
        DELIVERED = "3", "Delivered"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=ORDER_STATUS, default=ORDER_STATUS.PENDING, max_length=1
    )

    def __str__(self):
        return f"{self.user.name} order at {self.orderDate} with status {self.status} "


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product} from order number {self.order.id}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.full_name} have {self.product.name} in his cart"
