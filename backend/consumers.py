from drf_async.mixins import DRFJsonConsumerMixinAsync
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import random
from channels.db import database_sync_to_async
from .models import *
from .serializers import *
from asgiref.sync import sync_to_async


class NotificationsConsumer(AsyncJsonWebsocketConsumer,DRFJsonConsumerMixinAsync):

    async def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        self.group_name = self.username
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
    async def receive_json(self, content):
        
        await self.update_notifications(content)

    async def update_notifications(self, event):
        
        notifications = await self._update_notifications(event)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


    @database_sync_to_async
    def _update_notifications(self, content):
        get_user = User.objects.get(username=content['user'])
        instance =  Notifications.objects.filter(user_from=get_user).values('id','sender','user_from','actions')
        for x in instance:
            x['views']=True
            i = Notifications.objects.get(id=x['id'])
            if i.views is True:
                return i
            else:
                serializer = NotificationsSerializers(data=x)
                serializer.is_valid(raise_exception=True)
                notifications = serializer.update(i, serializer.validated_data)
        return notifications
    

class ChatConsumer(AsyncJsonWebsocketConsumer,DRFJsonConsumerMixinAsync):

    async def connect(self):
        self.roomname = self.scope['url_route']['kwargs']['roomname']
        self.group_name = self.roomname
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
    async def receive_json(self, content):
        print(content)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
