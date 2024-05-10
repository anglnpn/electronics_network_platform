import os
from dotenv import load_dotenv

from django.core.management import BaseCommand

from users.models import User

load_dotenv()


class Command(BaseCommand):
    """
    Команда для создания пользователя.
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('USER_EMAIL'),
            name=os.getenv('USER_NAME'),
            surname=os.getenv('USER_SURNAME'),
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('USER_PASSWORD'))
        user.save()
