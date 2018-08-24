# Import libraris and modules
import datetime
from dateutil.relativedelta import *
from django.conf import settings
from django.utils import crypto as pwdgen
from modules import osauth

from chance import chance

print("Starting Portal OpenStack Dev population script...")

def run():
    for p in range(0,20):
        projectname = chance.word().upper()
        projectdescription = chance.sentence(language='en')
        department = chance.word().upper()
        username = chance.first().upper()
        password = pwdgen.get_random_string()
        firstname = username
        familyname = chance.last()
        emailaddress = chance.email()
        telephone = chance.phone(formatted=False)
        tos = True
        date_now = datetime.date.today()
        date = str(date_now)
        keystone = osauth.connect()
        keystone.projects.create(
                  name=projectname,
                  domain=settings.OPENSTACK_SANDBOX_DOMAIN,
                  description=projectdescription,
                  enabled=True,
                  department=department,
                  username=username,
                  firstname=firstname,
                  familyname=familyname,
                  emailaddress=emailaddress,
                  telephone=telephone,
                  tos=tos,
                  createddate=date,
                  sandbox=True
        )
        project_id = keystone.projects.find(name=projectname).id
        keystone.users.create(
                  name=username,
                  domain=settings.OPENSTACK_SANDBOX_DOMAIN,
                  default_project=project_id,
                  password=password,
                  email=emailaddress,
                  description="Sandbox User",
                  firstname=firstname,
                  familyname=familyname,
                  emailaddress=emailaddress,
                  telephone=telephone,
                  enabled=True,
                  createddate=date,
                  sandbox=True
        )
        role_id = keystone.roles.find(name='Member')
        user_id = keystone.users.find(name=username).id
        keystone.roles.grant(role_id, user=user_id, project=project_id)
