from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'jokes-home'),
    path('about/', views.about, name = 'jokes-about')
]