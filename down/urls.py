from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'down-home'),
    path('about/', views.about, name = 'down-about')
]