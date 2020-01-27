from .old_settings import *

# Add user_unique_email to INSTALLED_APPS
INSTALLED_APPS.append('user_unique_email')

# Custom User model
AUTH_USER_MODEL = 'user_unique_email.User'
