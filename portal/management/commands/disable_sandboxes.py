# Import library and modules
from django.core.management.base import BaseCommand
import datetime
from dateutil.relativedelta import *
from django.conf import settings
from modules import osauth

class Command(BaseCommand):
    help = 'Disable Sandboxes Older than PROJECT_EXPIRY Days'
    def handle(self, *args, **kwargs):
        print("Starting Project expiry ...")
        keystone = osauth.connect()
        exp_days = int(settings.PROJECT_EXPIRY)
        date_today = datetime.date.today()
        disabled_date = str(date_today)
        proj_list = keystone.projects.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN, enabled=True)
        for p in proj_list:
            if hasattr(p, 'sandbox'):
                proj_date = datetime.date(*[int(i) for i in p.createddate.split("-")])
                if proj_date < date_today - relativedelta(days=exp_days):
                    keystone.projects.update(p.id, enabled=False, disabled_date=disabled_date)
                    print("Disabling Project: " + p.name)
        print("")
        print("Project expiry Complete...")
        print("")
        print("")
        print("Starting User expiry ...")
        user_list = keystone.users.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN, enabled=True)
        for u in user_list:
            if hasattr(u, 'sandbox'):
                user_date = datetime.date(*[int(i) for i in p.createddate.split("-")])
                if user_date < date_today - relativedelta(days=exp_days):
                    keystone.users.update(u.id, enabled=False, disabled_date=disabled_date )
                    print("Disabling User: " + u.name)
        print("")
        print("User expiry Complete...")
