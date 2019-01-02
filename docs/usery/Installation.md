---
layout: default
---
# Usery Portal for Cloud Sandboxes
## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites

### Usery

* You need [Docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/v17.09/compose/install/#install-compose) installed.
* Postgresql Database (9.6 used for development)
    * [Follow these instructions](./docs/postgres/postgres_install.md) to install postgresql with docker-compose.
* Dedicated Openstack Domain for Sandboxes
*  Clone this repository to your local machine
```
git clone git@github.com:lhaig/usery.git
```

## Installing
### Using Docker
Change directory into docs/docker
```
cd docs/docker
```

Copy the .env.example file and edit it.
```
cp .env.example .env
```
Edit the file
```
SECRET_KEY=[GENERATE A NEW KEY]
OPENSTACK_USERNAME='admin'
OPENSTACK_PASSWORD='secret'
OPENSTACK_PROJECTNAME='admin'
OPENSTACK_AUTHURL='http://172.16.100.10/identity/v3'
OPENSTACK_HORIZONURL='http://172.16.100.10/dashboard'
OPENSTACK_SANDBOX_DOMAIN='default'
OPENSTACK_USER_DOMAIN_NAME='default'
OPENSTACK_PROJECT_DOMAIN_NAME='default'
FROM_EMAIL='usery_portal@example.com'
SUPPORT_EMAIL='cloud_support@example.com')
PROJECT_EXPIRY='1'
PROJECT_DELETE='1'
DATABASE_NAME='pgtest'
DATABASE_USER='pgtest'
DATABASE_PASSWORD='wai2Rain'
DATABASE_HOST='127.0.0.1'
DATABASE_PORT=5432
EMAIL_HOST='IP_EMAIL_HOST'
ALLOWED_HOSTS=.localhost, .internal_server.com
```
1. replace 'PGCONTAINERNAME' with the container name you want.
2. replace all the other settings with the ones for your environment.
3. Generate a new SECRET-KEY using this command
  3.1.
      ```
      python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
      ```
4. Set the 'PROJECT_EXPIRY' setting to the number of days a project is alive for before it is disabled.
5. Set the 'PROJECT_DELETE' setting to the number of days after a project is disabled that the project will be deleted.
6. set the email host to the SMTP relay that will be used to send email.

### Cron jobs for disabling and deleting projects

In the .env file add your desired expiry in days the default is disable after 30 days and then delete 30 days later

To configure the cron job use this example

```
# m h  dom mon dow   command
0 4 * * * /bin/python3 /srv/usery/usery/manage.py disable_sandboxes
0 5 * * * /bin/python3 /srv/usery/usery/manage.py delete_sandboxes
```

[back](./)
