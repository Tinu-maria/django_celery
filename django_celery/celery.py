import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
# You use .setdefault() of os.environ to assure that your Django project’s settings.py module is accessible through the "DJANGO_SETTINGS_MODULE" key

app = Celery("django_celery")
# You create the Celery application instance and provide the name of the main module as an argument

app.config_from_object("django.conf:settings", namespace="CELERY")
# You define the Django settings file as the configuration file for Celery and provide a namespace, "CELERY"

app.autodiscover_tasks()
# You tell your Celery application instance to automatically find all tasks in each app of your Django project


# Producer: Your Django app
# Message Broker: The Redis server
# Consumer: Your Celery app