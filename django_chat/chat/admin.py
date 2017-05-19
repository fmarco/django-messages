# -*- coding: utf-8 -*-
from django.contrib import admin
from .utils import get_message_model

Message = get_message_model()


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
