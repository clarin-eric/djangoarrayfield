import django_arrayfield
from django.apps import AppConfig


class DjangoArrayConfig(AppConfig):
    name = djangoarrayfield.__name__
    verbose_name = 'Django Array Field'
