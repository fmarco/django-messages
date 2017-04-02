from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured

from .app_settings import app_settings


def get_message_model():
    """
    Returns the Message model that is active in this project.
    """
    path = app_settings.MESSAGE_MODEL
    try:
        return django_apps.get_model(path)
    except ValueError:
        raise ImproperlyConfigured(
            "path must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "path refers to model '%s' that\
             has not been installed" % app_settings.MESSAGE_MODEL
        )
