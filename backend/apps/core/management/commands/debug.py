from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run debug code'

    def handle(self, *args, **options):
        print('Debug django call functions')