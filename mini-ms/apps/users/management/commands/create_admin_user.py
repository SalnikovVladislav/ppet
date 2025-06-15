import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from dotenv import load_dotenv


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        load_dotenv()

        username = "admin"
        email = "admin@adm.ru"
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'secret-key')

        if not password:
            self.stderr.write(self.style.ERROR("DJANGO_SUPERUSER_PASSWORD не задан"))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Суперпользователь '{username}' создан."))
        else:
            self.stdout.write(self.style.WARNING(f"Суперпользователь '{username}' уже существует."))