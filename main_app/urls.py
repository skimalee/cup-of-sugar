from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('cups/', views.index, name='index'),
    path('chats/', views.chats_index, name='chats_index'),
    path('cups/<int:pk>', views.CupRead.as_view(), name='detail'),
    path('cups/create/', views.CupCreate.as_view(), name='cups_create'),
    path('cups/<int:pk>/update', views.CupUpdate.as_view(), name='cups_update'),
    path('cups/<int:pk>/delete', views.CupDelete.as_view(), name='cups_delete'),
]
