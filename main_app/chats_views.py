from django.shortcuts import render
from . models import Profile

# Create your views here.


def chats_index(request):
    profile = Profile.objects.get(user=request.user.id)
    chats = profile.chats.all()
    print('we did it!')
    return render(request, 'main_app/chats_index.html', {'profile': profile, 'chats': chats})
