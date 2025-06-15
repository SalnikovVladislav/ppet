from django.db import models
from apps.users.models import User
from apps.common.models.base import BaseModel


class Dialog(BaseModel):
    participants = models.ManyToManyField(User, related_name="dialogs")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dialog #{self.id}"