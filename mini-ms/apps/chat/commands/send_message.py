from apps.chat.models import Message


class SendMessageCommand:
    def __init__(self, sender, dialog, text):
        self.sender = sender
        self.dialog = dialog
        self.text = text

    def execute(self):
        return Message.objects.create(
            sender=self.sender,
            dialog=self.dialog,
            text=self.text
        )