from django.forms import ModelForm
from .models import Message, Chat


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = []
