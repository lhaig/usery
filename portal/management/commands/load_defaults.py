# Import library and modules
from django.core.management.base import BaseCommand
from django.conf import settings
from portal.models import SandbStatic

class Command(BaseCommand):
    help = 'Populate Usery with Default Data'
    def handle(self, *args, **kwargs):
        print("Starting Portal Default Data script...")
        SandbStatic.objects.create(name = 'Description', sandb_static = 'Describe your Cloud')
        SandbStatic.objects.create(name = 'Tos', sandb_static = 'Add your Terms Of Service')
        SandbStatic.objects.create(name = 'HomeStatic', sandb_static = 'Add Default home page text')
