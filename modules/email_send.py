from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_email(from_email, to, firstname, familyname, username, password, horizon_url, sandbox_domain):
    subject = "Usery Sandbox Portal Details"
    to = [to]
    from_email = from_email
    ctx = {
        'firstname': firstname,
        'familyname': familyname,
        'username': username,
        'password': password,
        'horizon_url': horizon_url,
        'sandbox_domain': sandbox_domain
    }
    message = render_to_string('email/welcome.txt', ctx)
    EmailMessage(subject, message, to=to, from_email=from_email).send()

def send_support_team_email(from_email, to, firstname, familyname, project, description, telephone):
    subject = "New Usery Sandbox User Details"
    to = [to]
    from_email = from_email
    ctx = {
        'firstname': firstname,
        'familyname': familyname,
        'project': project,
        'description': description,
        'telephone': telephone
    }
    message = render_to_string('email/support_team.txt', ctx)
    EmailMessage(subject, message, to=to, from_email=from_email).send()
