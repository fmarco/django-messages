# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from channels import Group


class Message(models.Model):
    room = models.CharField(max_length=20)
    message = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def send_notification(self):
        Group(self.room).send(
            {
                "text": self.message
            }
        )

    def __str__(self):
        return 'Message on room {0} by user {1}'.format(self.room, self.user.username)


@receiver(post_save, sender=Message, dispatch_uid="broadcast_message")
def broadcast_message(sender, instance, **kwargs):
    if kwargs['created']:
        instance.send_notification()
