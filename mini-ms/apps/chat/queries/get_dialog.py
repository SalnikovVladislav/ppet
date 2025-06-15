from apps.chat.models import Dialog
from apps.users.models import User


def get_or_create_dialog(user1: User, user2: User):
    dialogs = Dialog.objects.filter(participants=user1).filter(participants=user2)
    if dialogs.exists():
        return dialogs.first()

    dialog = Dialog.objects.create()
    dialog.participants.add(user1, user2)
    return dialog
