from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import Profile, Message, Chat

# Create your views here.


@login_required
def chats_index(request):
    chats = []
    last_messages = []
    profile = request.user.profile
    chats_beta = profile.chats.order_by('-message__created_at')
    for chat in chats_beta:
        if chat in chats:
            pass
        elif chat not in chats:
            chats.append(chat)
    for chat in chats:
        last_messages.append(chat.message_set.first())
    return render(request, 'chats/index.html', {'profile': profile, 'chats': chats, 'last_messages': last_messages})


@login_required
def chats_detail(request, chat_id):
    profile = request.user.profile
    chat = Chat.objects.get(id=chat_id)
    messages = chat.message_set.all()
    messages = messages.order_by('-created_at')
    print(messages)
    return render(request, 'chats/detail.html', {'profile': profile, 'chat': chat, 'messages': messages})
