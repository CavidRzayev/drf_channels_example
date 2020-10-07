from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date  = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
    
class DirectMessage(Chat):
    user_to = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_to.username
    


class Notifications(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='senders',blank=True, null=True)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE,related_name='me',blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    actions = models.CharField(max_length=200)
    views = models.BooleanField(default=False)

    def __str__(self):
        return self.actions
    


    