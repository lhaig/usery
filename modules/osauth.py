from keystoneauth1.identity import v3
from keystoneauth1 import session as keystone_session
from keystoneclient.v3 import client
from keystoneclient import utils
from django.conf import settings

def connect():
    auth = v3.Password(
        auth_url=settings.OPENSTACK_AUTHURL,
        username=settings.OPENSTACK_USERNAME,
        password=settings.OPENSTACK_PASSWORD,
        project_name=settings.OPENSTACK_PROJECTNAME,
        user_domain_name=settings.OPENSTACK_USER_DOMAIN_NAME,
        project_domain_name=settings.OPENSTACK_PROJECT_DOMAIN_NAME
		)
    session = keystone_session.Session(auth=auth,verify=False)
    keystone = client.Client(session=session,interface="public")
    return (keystone)
