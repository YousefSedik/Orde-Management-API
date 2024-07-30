from django.core.management.base import BaseCommand
from core.models import Product, Cart, Product
from faker import Faker
from random import randint, choice

# get user model
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Generate orders for cart"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of cart to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for _ in range(total):
            random_product = Product.objects.order_by("?").first()
            random_user = User.objects.order_by("?").first()
            Cart.objects.create(
                user=random_user, product=random_product, quantity=randint(1, 10)
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully created {total} cart"))
