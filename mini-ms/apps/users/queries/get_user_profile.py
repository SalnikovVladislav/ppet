from apps.users.models import User

class GetUserProfileQuery:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def execute(self):
        try:
            user = User.objects.get(id=self.user_id)
            return user
        except User.DoesNotExist:
            return None