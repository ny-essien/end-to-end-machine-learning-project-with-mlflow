from django.contrib import admin
from .models import Topic, Room, Messages

# Register your models here.
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Messages)
