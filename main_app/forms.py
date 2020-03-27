from django.forms import ModelForm
from .models import Message, Chat, Cup


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = []


class CupForm(ModelForm):
    class Meta:
        model = Cup
        fields = ['cup_type', 'item', 'description', 'category']
