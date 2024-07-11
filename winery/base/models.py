from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Room(models.Model):

    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    description = models.TextField(max_length=200, blank=False, null = False)
    host = models.ForeignKey(User, on_delete= models.CASCADE)
    participants = ""
    date_created = models.DateTimeField(auto_now= True)
    updated = models.DateTimeField(auto_now_add= True)

    class Meta:

        ordering = ["date_created", "updated"]

    def __str__(self):
        return self.name

class Messages(models.Model):

    room = models.ForeignKey(Room, on_delete= models.SET_NULL, null = True)
    message = models.TextField(max_length= 200, blank = False, null = False)
    date_created = models.DateTimeField(auto_now= True)
    updated = models.DateTimeField(auto_now_add= True)

    class Meta:

        ordering = ["date_created", "updated"]

    def __str__(self):
        return self.message[:100]




