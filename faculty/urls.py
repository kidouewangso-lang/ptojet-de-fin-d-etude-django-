from django.urls import path
from . import views

from django.shortcuts import redirect

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile.html', lambda request: redirect('dashboard')),
    path('dashboard/index.html', lambda request: redirect('dashboard')),
]
