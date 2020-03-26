from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import Profile, Message, Chat

# Create your views here.

@login_required
def chats_index(request):
    profile = Profile.objects.get(user=request.user.id)
    chats = profile.chats.order_by('-message__created_at')
    # chats = profile.chats.order_by('-message_set__created_at')
    # chats = profile.chats.order_by('-updated_at')
    print(chats)
    return render(request, 'chats/index.html', {'profile': profile, 'chats': chats})

