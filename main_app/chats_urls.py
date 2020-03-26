from django.urls import path
from . import chats_views

urlpatterns = [
    path('', chats_views.chats_index, name='chats_index'),
    path('<int:chat_id>/', chats_views.chats_detail, name='chats_detail'),
    path('create/', chats_views.chats_create, name='chats_create'),
    path('<int:chat_id>/add_message/', chats_views.add_message, name='add_message'),
]
