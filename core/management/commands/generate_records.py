import random
from faker import Faker
from django.core.management.base import BaseCommand
from core.models import Product

# decorator to calculate the time taken by the function
from time import time


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"Time taken: {end-start}")

    return inner


class Command(BaseCommand):

    help = "Generate random products using Faker"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of products to be created"
        )

    @calculate_time
    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        names = [
            "apple",
            "banana",
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grape",
            "honeydew",
            "kiwi",
            "lemon",
            "mango",
            "nectarine",
            "orange",
            "papaya",
            "quince",
            "raspberry",
            "strawberry",
            "tangerine",
            "watermelon",
        ]
        discr = [
            "this is a description",
            "this is another description",
            "this is a description too",
            "this is a description as well",
        ]
        for _ in range(total):

            name = random.choice(names)
            description = random.choice(discr)
            price = 13.99
            stock = 312
            Product.objects.create(
                name=name, description=description, price=price, stock=stock
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully created {total} products"))
