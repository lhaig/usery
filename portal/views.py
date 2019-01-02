from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ValidationError
from django.utils import crypto as pwdgen
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
import datetime
from dateutil.relativedelta import *
from modules import osauth
from modules import email_send as mail
from .forms import CreateOpenstackSandboxProjectForm
from .models import SandbStatic

def home(request):
    # Sets up th ehome view with data from openstack
    keystone = osauth.connect()
    proj = keystone.projects.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)
    all_users = keystone.users.list(domain=settings.OPENSTACK_SANDBOX_DOMAIN)
    sandb = []
    usrs = []
    number_sandb = 0
    number_usrs = 0
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
    home_static = SandbStatic.objects.get(name='HomeStatic')
    return render(request, 'home.html', {'sandboxes': number_sandb, 'sandbox_users': number_usrs, 'home_static': home_static })

def terms_of_use(request):
    tos_content = SandbStatic.objects.get(name='Tos')
    return render(request, 'terms_of_use.html', {'tos_content': tos_content})

def cloud_description(request):
    descript = SandbStatic.objects.get(name='Description')
    return render(request, 'cloud_description.html', {'descript': descript})

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
            mail.send_email(settings.FROM_EMAIL, emailaddress, firstname, familyname, username, password, settings.OPENSTACK_HORIZONURL, settings.OPENSTACK_SANDBOX_DOMAIN)
            mail.send_support_team_email(settings.FROM_EMAIL, settings.SUPPORT_EMAIL, firstname, familyname, projectname, projectdescription, telephone)

            return redirect('request_project')
    tos_content = SandbStatic.objects.get(name='Tos')
    return render(request, 'request_project.html', { 'form': form, 'tos_content': tos_content })

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

@method_decorator(staff_member_required, name='dispatch')
class list_static(ListView):
    model = SandbStatic
    context_object_name = 'static_pages'
    template_name = 'static_list.html'

@method_decorator(staff_member_required, name='dispatch')
class edit_static(UpdateView):
    model = SandbStatic
    fields = ['name', 'sandb_static']
    template_name = 'static_edit.html'
    success_url = reverse_lazy('list_static')

@method_decorator(staff_member_required, name='dispatch')
class view_static(DetailView):
    model = SandbStatic
    template_name = 'static_view.html'
