# -*- coding: utf-8 -*-
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http

from .utils import get_message_model
from .app_settings import app_settings

Message = get_message_model()

ACCEPTED = {"accept": True}
CLOSED = {"close": True}


@channel_session_user_from_http
def connect(message):
    if app_settings.CHECK_AUTH and not message.user.is_authenticated():
        message.reply_channel.send(CLOSED)
    else:
        message.reply_channel.send(ACCEPTED)
        room = message.content['path'].strip("/")
        message.channel_session['room'] = room
        Group(room).add(message.reply_channel)


@channel_session_user
def disconnect(message):
    Group(message.channel_session['room']).discard(message.reply_channel)


@channel_session_user
def send_message(message):
    room = message.channel_session['room']
    Group(room).send(
        {
            "text": message.content['text']
        }
    )
    if app_settings.SAVE_ON_DB:
        Message.objects.create(
            room=room,
            message=message.content['text'],
            user=message.user
        )
