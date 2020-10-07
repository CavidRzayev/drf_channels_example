from django.urls import re_path
from .consumers import *


websocket_urlpatterns = [
    re_path(r'not/(?P<username>\w+)/$', NotificationsConsumer),
    re_path(r'room/(?P<roomname>\w+)/$', ChatConsumer),
    
]