from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
import datetime
from dateutil.relativedelta import *
from django.core.exceptions import ValidationError
from django.utils import crypto as pwdgen
from django.contrib.auth.decorators import login_required
from django.conf import settings
from modules import osauth
from modules import email_send as mail
from .forms import CreateOpenstackSandboxProjectForm

def home(request):
    # Sets up th ehome view with data from openstack
    keystone = osauth.connect()
    proj = keystone.projects.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)
    all_users = keystone.users.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)
    sandb = []
    usrs = []
    # returns the number of sandbox projects
    for p in proj:
        if hasattr(p, 'sandbox'):
            sandb.append(p)
            number_sandb = len(sandb)
    # returns the number of sandbox users
    for u in all_users:
        if hasattr(u, 'sandbox'):
            usrs.append(p)
            number_usrs = len(usrs)
    return render(request, 'home.html', {'sandboxes': number_sandb, 'sandbox_users': number_usrs })

def terms_of_use(request):
    return render(request, 'terms_of_use.html')

def cloud_description(request):
    return render(request, 'cloud_description.html')

def request_project(request):
    form = CreateOpenstackSandboxProjectForm
    # Gets all the information from the form and creates the project and user
    if request.method == 'POST':
        form = form(data=request.POST)
        if form.is_valid():
            projectname = request.POST.get('projectname', '').upper()
            projectdescription = request.POST.get('projectdescription', '')
            department = request.POST.get('department', '')
            username = request.POST.get('username', '').upper()
            password = pwdgen.get_random_string()
            firstname = request.POST.get('firstname', '')
            familyname = request.POST.get('familyname', '')
            emailaddress = request.POST.get('emailaddress', '')
            telephone = request.POST.get('telephone', '')
            tos = request.POST.get('tos', '')
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
            # Emails the user and the support team
            mail.send_email(settings.FROM_EMAIL, emailaddress, firstname, familyname, username, password, settings.OPENSTACK_HORIZONURL)
            mail.send_support_team_email(settings.FROM_EMAIL, settings.SUPPORT_EMAIL, firstname, familyname, projectname, projectdescription, telephone)

            return redirect('request_project')
    return render(request, 'request_project.html', { 'form': form, })

@staff_member_required
def project_list(request):
    keystone = osauth.connect()
    proj = keystone.projects.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)
    projects=[]
    for p in proj:
        if hasattr(p, 'sandbox'):
            projects.append(p)
    return render(request, 'project_list.html', {'projects': projects})

@staff_member_required
def project_detail(request):
    proj_id = request.GET.get('proj')
    keystone = osauth.connect()
    project = keystone.projects.get(proj_id)
    return render(request, 'project_detail.html', {'project': project})

@staff_member_required
def sandbox_user_list(request):
    keystone = osauth.connect()
    sandbox_user = keystone.users.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)
    sandbox_users=[]
    for u in sandbox_user:
        if hasattr(u, 'sandbox'):
            sandbox_users.append(u)
    return render(request, 'sandbox_user_list.html', {'sandbox_users': sandbox_users})
