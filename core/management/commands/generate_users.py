# create users using Faker
import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):

    help = "Generate random users using Faker"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of users to be created"
        )

    def handle(self, *args, **kwargs):

        total = kwargs["total"]
        faker = Faker()
        for _ in range(total):
            first_name = faker.first_name()
            last_name = "patata"
            # username = faker.unique.user_name()
            email = faker.unique.email()
            password = "this is weierd password"
            try:
                User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    # username=username,
                    email=email,
                    password=password,
                )
            except:
                print("email already exists")

        self.stdout.write(self.style.SUCCESS(f"Successfully created {total} users"))
