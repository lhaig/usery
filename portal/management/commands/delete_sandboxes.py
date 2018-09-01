# Import library and modules
from django.core.management.base import BaseCommand
import datetime
from dateutil.relativedelta import *
from django.conf import settings
from modules import osauth

class Command(BaseCommand):
    help = 'Delete Sandboxes Older than PROJECT_DELETE Days'
    def handle(self, *args, **kwargs):
        print("Starting Project delete ...")
        keystone = osauth.connect()
        del_days = int(settings.PROJECT_DELETE)
        date_today = datetime.date.today()

        disabled_proj_list = keystone.projects.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN, enabled=False)
        for p in disabled_proj_list:
            if hasattr(p, 'sandbox'):
                proj_date = datetime.date(*[int(i) for i in p.disabled_date.split("-")])
                if proj_date < date_today - relativedelta(days=del_days):
                    keystone.projects.delete(p.id)
                    print("Deleting Project: " + p.name)
        print("")
        print("Project delete Complete...")
        print("")
        print("")
        print("Starting User delete ...")
        disabled_user_list = keystone.users.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN, enabled=False)
        for u in disabled_user_list:
            if hasattr(u, 'sandbox'):
                user_date = datetime.date(*[int(i) for i in p.disabled_date.split("-")])
                if user_date < date_check - relativedelta(days=del_days):
                    keystone.users.delete(u.id)
                    print("Deleting User: " + u.name)
        print("")
        print("User delete Complete...")
