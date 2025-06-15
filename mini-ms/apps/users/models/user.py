from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.common.models.base import BaseModel

class User(AbstractUser, BaseModel):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MANAGER = 'manager', 'Manager'
        EMPLOYER = 'employer', 'Employer'
        CLIENT = 'client', 'Client'

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.CLIENT,
    )

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_manager(self):
        return self.role == self.Role.MANAGER

    def is_employer(self):
        return self.role == self.Role.EMPLOYER

    def is_client(self):
        return self.role == self.Role.CLIENT