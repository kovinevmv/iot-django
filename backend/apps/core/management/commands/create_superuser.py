from django.core.management.base import BaseCommand

from backend.apps.core.models import get_or_none
from backend.apps.parent.models import Parent
from backend.settings import SUPERUSER


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        try:
            admin = SUPERUSER
            if not get_or_none(Parent, email=admin['email']):
                Parent.objects.create_superuser(**admin)
        except Exception as e:
            print(e)