from django import forms
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from keystoneclient.exceptions import NotFound
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhonePrefixSelect
from modules import osauth

class CreateOpenstackSandboxProjectForm(forms.Form):
    projectname = forms.CharField(
        label='Project Name',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Project Name','style':'width: 100%'}),
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='Project Name must be Letters and Numbers Only',
                code='invalid_projectname',
            ),
        ],
    )
    projectdescription = forms.CharField(
        label='Project Description (Max 500)',
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Project Description','style':'height: 100px'}),
        max_length=500,
        required=True,
    )
    department = forms.CharField(
        label='Department',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Department','style':'width: 100%'}),
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='Department Name must be Alphanumeric',
                code='invalid_departmentname',
            ),
        ],
    )
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Provide a Username','style':'width: 100%'}),
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='User Name must be Alphanumeric',
                code='invalid_username',
            ),
        ],
    )
    firstname = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name','style':'width: 100%'}),
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='First Name must be Alphanumeric',
                code='invalid_firstname',
            ),
        ],
    )
    familyname = forms.CharField(
        label='Family Name',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Family Name','style':'width: 100%'}),
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='Name must be Alphanumeric',
                code='invalid_familyname',
            ),
        ],
    )
    emailaddress = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address','style':'width: 100%'}),
    )
    telephone = PhoneNumberField(
        label='Telephone Number',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telehone Number','style':'width: 100%'}),
    )
    tos = forms.BooleanField(
        label='Terms Of Service',
        required=True,
        widget=forms.widgets.CheckboxInput(),
    )

    def clean_emailaddress(self):
        submitted_data = self.cleaned_data['emailaddress']
        return submitted_data

    def clean_projectname(self):
        submitted_data = self.cleaned_data['projectname']
        newproj = submitted_data.upper()
        keystone = osauth.connect()
        try:
            project = keystone.projects.find(name=newproj)
            raise forms.ValidationError('The project name is already taken')
        except NotFound:
            return submitted_data

    def clean_username(self):
        submitted_data = self.cleaned_data['username']
        uname = submitted_data.upper()
        keystone = osauth.connect()
        try:
            username = keystone.users.find(name=uname)
            raise forms.ValidationError('The user name is already taken')
        except NotFound:
            return submitted_data
