# -*- coding: utf-8 -*-
from channels.routing import route
from chat.consumers import connect, disconnect, send_message

channel_routing = [
    route("websocket.connect", connect),
    route("websocket.receive", send_message),
    route("websocket.disconnect", disconnect)
]
