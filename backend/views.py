from django.shortcuts import render
from django.shortcuts import render
from drf_async.jsonasync import AzPUG
from .models import *
from .serializers import *

class Notifications(AzPUG):
    model = Notifications
    stream = 'notifications'
    serializer = NotificationsSerializers

    @classmethod
    def group_names(cls, instance):
        
        return [instance.user_from.username]
        

class Chat(AzPUG):
    model = Chat
    stream = 'Chat'
    serializer = ChatSerializers

    @classmethod
    def group_names(cls, instance):
        
        return [instance.room.name]

def index(request):

    username = request.user.username
    context = {
        'username': username
    }
    return render(request,'index.html', context)


def room(request,roomname):
    get_room = Room.objects.get_or_create(name=roomname)
    context = {
        'roomname':roomname
    }
    return render(request,'room.html', context)