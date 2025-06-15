from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.commands.register_user import RegisterUserCommand
from apps.users.serializers.registration_serializer import RegistrationSerializer
from apps.users.serializers.user_serializer import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        command = RegisterUserCommand(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data['email'],
        )

        user = command.execute()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)