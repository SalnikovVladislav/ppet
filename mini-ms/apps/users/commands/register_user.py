from apps.users.models import User
from django.core.exceptions import ValidationError


class RegisterUserCommand:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def execute(self):
        if User.objects.filter(username=self.username).exists():
            raise ValidationError("Пользователь с таким именем уже существует")

        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            role='client',
        )
        return user