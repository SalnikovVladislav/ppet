import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from apps.users.models import User
from apps.chat.commands.send_message import SendMessageCommand
from apps.chat.queries.get_dialog import get_or_create_dialog


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.other_user_id = self.scope['url_route']['kwargs']['user_id']
        self.user = self.scope['user']
        self.other_user = await self.get_user(self.other_user_id)

        self.dialog = await database_sync_to_async(get_or_create_dialog)(self.user, self.other_user)
        self.room_group_name = f"chat_{self.dialog.id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        text = data['text']

        message = await database_sync_to_async(SendMessageCommand(
            sender=self.user,
            dialog=self.dialog,
            text=text
        ).execute)()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "sender": self.user.username,
                "text": text,
                "created_at": str(message.created_at)
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def get_user(self, user_id):
        return User.objects.get(id=user_id)
