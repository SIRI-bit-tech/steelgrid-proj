from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.exists():
            self.stdout.write('Superuser already exists')
            return

        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@steelgridsystems.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write('Superuser password not set in environment variables')
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write('Superuser created successfully') 