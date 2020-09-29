# rest-api-seed
![Python](https://img.shields.io/badge/restapi-v1.0.0-orange)![Python](https://img.shields.io/badge/flask-v1.1.2-blue)
![Python](https://img.shields.io/badge/flaskrestx-0.2.0-blue)
![Python](https://img.shields.io/badge/celery-v4.4.5-blue)
![Python](https://img.shields.io/badge/flower-v0.9.4-blue)
![Python](https://img.shields.io/badge/gunicorn-v19.7.1-blue)
![Python](https://img.shields.io/badge/pymsteams-v0.1.13-blue)
![Python](https://img.shields.io/badge/python-v3.7-blue)
![Python](https://img.shields.io/badge/platform-linux--64%7Cwin--64-lightgrey)

This service implements a scalable rest-api seed using flask and flask-restx. Information from different apps is loaded from *src/config/settings.py*. Different endpoints were develped in order to have templates for a variety of features, for example:

- Async tasks: Celery with RabbitMQ as message broker
- Users CRUD: SQLAlchemy and Flask models
- Microsoft Teams: Pymsteams and requests

**Content**
- [Getting started](#getting-started)
- [Endpoints](#endpoints)
- [Mock server](#mock-server)
- [Build](#docker)
- [Run](#run)
- [References](#references)


## Getting started

Dir structure of repo
```
├── dashboard
├── mock-server
└── src
    ├── config
    ├── logs
    ├── services
    └── utilities

7 directories
```
