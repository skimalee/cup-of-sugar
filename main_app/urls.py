from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cups/', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('cups/<int:pk>', views.CupRead.as_view(), name='cups_read'),
]
