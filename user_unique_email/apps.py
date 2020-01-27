from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserUniqueEmailConfig(AppConfig):
    name = 'user_unique_email'
    verbose_name = _("Authentication and Authorization")
