from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.users.queries.get_user_profile import GetUserProfileQuery
from apps.users.serializers.user_serializer import UserSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = GetUserProfileQuery(user_id=request.user.id)
        user = query.execute()
        return Response(UserSerializer(user).data)