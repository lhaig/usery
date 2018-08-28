# Import library and modules
from django.core.management.base import BaseCommand
import datetime
from dateutil.relativedelta import *
from django.conf import settings
from django.utils import crypto as pwdgen
from modules import osauth

from chance import chance

class Command(BaseCommand):
    help = 'Delete Usery Sample Data'
    def handle(self, *args, **kwargs):
        print("Starting Portal OpenStack Dev deletion script...")
        keystone = osauth.connect()
        sand_proj = keystone.projects.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)
        sand_users = keystone.users.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)

        for u in sand_users:
            if hasattr(u, 'sandbox'):
                keystone.users.delete(u)
                self.stdout.write(self.style.SUCCESS('User "%s" deleted with success!' % u.name))

        for p in sand_proj:
            if hasattr(p, 'sandbox'):
                keystone.projects.delete(p)
                self.stdout.write(self.style.SUCCESS('Project "%s" deleted with success!' % p.name))
