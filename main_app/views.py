from django.shortcuts import render, redirect
from . models import Cup, Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CupCreate(LoginRequiredMixin, CreateView):
    model = Cup
    fields = ['cup_type', 'item', 'description', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CupRead(LoginRequiredMixin, DetailView):
    model = Cup
    fields = ['user_name', 'cup_type', 'item',
              'category', 'description', 'fulfilled']


class CupUpdate(LoginRequiredMixin, UpdateView):
    model = Cup
    fields = ['item', 'description', 'category']
    print('hello from cup update')

class CupDelete(LoginRequiredMixin, DeleteView):
    model = Cup
    success_url = '/cups/'


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['display_name', 'zip']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'zip']

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    fields = ['display_name', 'zip']

class ProfileRead(LoginRequiredMixin, DetailView):
    model = Profile
    fields = ['display_name', 'zip']

def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    cups = Cup.objects.all()
    return render(request, 'cups/index.html', {'cups': cups})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profiles_create')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

