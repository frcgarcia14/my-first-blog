# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
    #chat_room_id
    #name
    name = models.CharField(max_length=30)
    #created_at
    created_at = models.DateField()

    def __str__(self):
        return "%s" % (self.name)

class Message(models.Model):
     #Message_id
     #chat_room_id FK
     chat_room_id_fk = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
     #user_id FK
     user_id_fk = models.ForeignKey(User, on_delete=models.CASCADE)
     #message content
     message = models.CharField(max_length=300)
     #created_at
     created_at = models.DateField()

     def __str__(self):
        return "%s" % (self.message)
