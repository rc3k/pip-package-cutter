from decimal import Decimal

from django.utils.translation import gettext_lazy as _
from saas.app_config import BaseAppConfig


class {{cookiecutter.app_name.capitalize()}}Config(BaseAppConfig):
    name = "{{cookiecutter.app_name}}"
    verbose_name = "{{cookiecutter.project_name}}"
    version = '{{cookiecutter.version}}'
    roles = []
    _auto_install = True
