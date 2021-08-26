from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='memes-home'),
    path('about/', views.about, name="memes-about"),
    path('<int:id>/', views.show, name='show-meme'),
    path('new/', views.create, name='create-meme')
]