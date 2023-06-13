from saas.app_config import BaseAppConfig


class {{cookiecutter.app_name.capitalize()}}Config(BaseAppConfig):
    name = "{{cookiecutter.app_name}}"
    verbose_name = "{{cookiecutter.project_name}}"
    version = 0.1
    roles = []
    _auto_install = True
