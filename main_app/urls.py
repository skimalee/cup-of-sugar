from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('cups/', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cups/<int:pk>', views.CupRead.as_view(), name='cups_read'),
    path('cups/create/', views.CupCreate.as_view(), name='cups_create'),
    path('cups/<int:pk>', views.CupUpdate.as_view(), name='cups_update'),
    path('cups/<int:pk>', views.CupDelete.as_view(), name='cups_delete'),
]
