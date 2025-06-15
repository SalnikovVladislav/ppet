from django.db import models
from apps.users.models import User
from apps.chat.models import Dialog
from apps.common.models.base import BaseModel


class Message(BaseModel):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_read = models.BooleanField(default=False)
