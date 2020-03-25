from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Profile

# Create your views here.

@login_required
def chats_index(request):
    profile = Profile.objects.get(user=request.user.id)
    chats = profile.chats.all()
    # chats = 
    print(profile.display_name)
    return render(request, 'chats/index.html', {'profile': profile, 'chats': chats})
