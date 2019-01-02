---
layout: default
---
# Deploying a postgres database.
## With Docker
You need [Docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/v17.09/compose/install/#install-compose) installed.

Copy the .env.example file and edit it.
```
cp .env.example .env
```
Edit the file
```
PG_CONTAINER_NAME=pgserver
PG_USER_NAME=pgtest
PG_USER_PWD=CHANGEME
PG_DB_NAME=pgtest
PG_DB_PATH=/tmp/dbfiles
```
1. replace 'pgserver' with the container name you want.
2. replace 'pgtest' with the usery db user.
3. replace 'CHANGEME' with the password you want to use for the db user.
4. replace 'pgtest' with the name you want to use for the database.
5. replace '/tmp/dbfiles' with the path on your system for database files to persist data.


# It is suggested that your database is configured in HA mode for production purposes.

[back](./)
