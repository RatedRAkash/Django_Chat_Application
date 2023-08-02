from django.urls import path, re_path
from chatApp import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server', consumers.MyChatWebSocketConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
    path('ws/<str:room_name>/', consumers.ChatRoomConsumer.as_asgi()),
]