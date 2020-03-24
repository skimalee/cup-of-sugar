from django.shortcuts import render, redirect
from . models import Cup, Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


class CupCreate(CreateView):
    model = Cup
    fields = ['cup_type', 'item', 'description', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CupRead(DetailView):
    model = Cup
    fields = ['user_name', 'cup_type', 'item',
              'category', 'description', 'fulfilled']


class CupUpdate(UpdateView):
    model = Cup
    fields = ['item', 'description', 'category']


class CupDelete(DeleteView):
    model = Cup
    success_url = '/cups/'


def home(request):
    return render(request, 'home.html')


def index(request):
    cups = Cup.objects.all()
    return render(request, 'cups/index.html', {'cups': cups})


def chats_index(request):
    profile = Profile.objects.get(user=request.user.id)
    chats = profile.chats.all()
    return render(request, 'main_app/chats_index.html', {'profile': profile, 'chats': chats})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
