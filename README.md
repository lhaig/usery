---
layout: default
---

# Usery Portal for Cloud Sandboxes
### This is Beta software at the moment
Usery is a portal to allow users to create themselves an openstack sandbox cloud project with no need for the cloud admins to do anything.
It will setup a project in the the cloud, create the user necessary for accessing this project and then email the user the login details.
It will also email the cloud support team to let them know of the new sandbox that has been created.

The portal needs a postgresql database to store the static file customization the Openstack metadata about the users and projects is stored within the object metadata.

## Integrations
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=lhaig/usery)](https://dependabot.com)
[![Open Source Helpers](https://www.codetriage.com/lhaig/usery/badges/users.svg)](https://www.codetriage.com/lhaig/usery)

## Getting Started
## Prerequisites
### Usery

* Postgresql Database (9.6 used for development)
    * [Follow these instructions](./docs/postgres/postgres_install.md) to install postgresql with docker-compose.
* Username and Password for the Postgresql database
* Dedicated Openstack Domain for Sandboxes

## Detailed Installation Instructions
* [Follow these instructions to get Usery up and running](./docs/usery/Installation.md)
## Development environment setup
* [Use this to setup a developent environment](./docs/usery/development.md)
* Colour Codes #ECC231 #CC973B #B17E3B

### Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/)
* [SB Admin 2 Template](https://startbootstrap.com/template-overviews/sb-admin-2/)

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/lhaig/usery/tags).

## Authors

* **Lance Haig** - *Initial work* - [lhaig](https://github.com/lhaig)

See also the list of [contributors](https://github.com/lhaig/usery/contributors) who participated in this project.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](./LICENSE) file for details

## Acknowledgments

* [Openstack developers](https://www.openstack.org/)
* [Vitor Freitas](https://simpleisbetterthancomplex.com)
* [JoeStack](https://github.com/joestack/)

## Screenshots

### Home Page
![Home](docs/images/home.png)
### Request Project
![Request](docs/images/project_request.png)
### Admin Dashboard
![Admin Dashboard](docs/images/admin_dashboard.png)
### Admin Project List
![Admin Project List](docs/images/admin_project_list.png)
### Admin Sandbox User List
![Admin Sandbox User List](docs/images/admin_sandbox_user_list.png)
### Admin Static Page List
![Admin Static Page List](docs/images/admin_static_page_list.png)
### Admin Static Page Edit
![Admin Static Page Edit](docs/images/admin_static_page_edit.png)
