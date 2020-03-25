from django.urls import path
from . import chats_views

urlpatterns = [
    path('', chats_views.chats_index, name='chats_index'),
]
