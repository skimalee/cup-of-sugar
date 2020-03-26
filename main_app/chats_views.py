from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Message, Chat
from .forms import MessageForm

# Create your views here.

@login_required
def chats_create(request, user_id):
    form = ChatForm(request.POST)
    if form.is_valid():
        new_chat = form.save(commit=False)
        new_chat.user1_id = request.user.id
        new_chat.user1_name = request.user.profile.display_name
        new_chat.user2_id = user_id
        new_chat.user2_name = Profile.objects.get(id=user_id).display_name
        new_chat.save()
        print(self)
        print(request)
    return redirect('chats_detail')



@login_required
def add_message(request, chat_id):
    form = MessageForm(request.POST)
    if form.is_valid():
        new_message = form.save(commit=False)
        new_message.chat = Chat.objects.get(id=chat_id)
        new_message.sender_name = request.user.profile.display_name
        new_message.sender_id = request.user.id
        new_message.save()
    return redirect('chats_detail', chat_id=chat_id)


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
    form = MessageForm()
    profile = request.user.profile
    chat = Chat.objects.get(id=chat_id)
    messages = chat.message_set.all()
    messages = messages.order_by('-created_at')
    return render(request, 'chats/detail.html', {'form': form,'profile': profile, 'chat': chat, 'messages': messages})