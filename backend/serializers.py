from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username',]

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields  = '__all__'


class ChatSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    room = RoomSerializers(read_only=True)

    class Meta:
        model = Chat
        fields  = '__all__'


class DirectSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_to = UserSerializer(read_only=True)

    model = DirectMessage
    fields = '__all__'
    
class NotificationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'