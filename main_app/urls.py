from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('cups/', views.index, name='index'),
    path('profile/<int:profile_id>', views.profile_detail, name='profile_detail'),
    path('profile/create', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profile/<int:pk>/delete', views.ProfileDelete.as_view(), name='profiles_delete'),
    path('cups/<int:pk>', views.CupRead.as_view(), name='detail'),
    path('cups/create/', views.CupCreate.as_view(), name='cups_create'),
    path('cups/<int:pk>/update', views.CupUpdate.as_view(), name='cups_update'),
    path('cups/<int:pk>/delete', views.CupDelete.as_view(), name='cups_delete'),
    path('cups/<int:cup_id>/add_photo/', views.add_photo, name='add_photo'),
]
