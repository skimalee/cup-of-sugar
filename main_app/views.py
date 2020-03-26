from django.shortcuts import render, redirect
from . models import Cup, Profile, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'cupofsugarone'
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
    print(request.user)
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

def add_photo(request, cup_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, cup_id=cup_id)
            print(cup_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', pk=cup_id)