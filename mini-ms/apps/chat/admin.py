from django.contrib import admin
from apps.chat.models import Dialog, Message

# Register your models here.
admin.site.register(Dialog)
admin.site.register(Message)