from django.core.management.base import BaseCommand
from core.models import Product, Cart, Order, OrderItem
from faker import Faker
from random import randint, choice

# get user model
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Generate orders for users"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of orders to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        faker = Faker()
        for _ in range(total):
            random_user = User.objects.order_by("?").first()
            description = faker.text(max_nb_chars=200)
            # generate fake datetime for orderDate
            orderDate = faker.date_time_this_year()
            order = Order.objects.create(
                user=random_user, orderDate=orderDate, status=choice(["1", "2", "3"])
            )
            for _ in range(randint(1, 10)):
                random_product = Product.objects.order_by("?").first()
                quantity = randint(1, 10)
                OrderItem.objects.create(
                    product=random_product, order=order, quantity=quantity
                )

        self.stdout.write(self.style.SUCCESS(f"Successfully created {total} orders"))
