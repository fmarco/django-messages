from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .app_settings import app_settings


class AbstractBaseMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    room = models.CharField(max_length=app_settings.ROOM_MAX_LENGTH)

    class Meta:
        abstract = True

    def send_notification(self):
        raise NotImplementedError(
            'You should implement the send_notification method'
        )
