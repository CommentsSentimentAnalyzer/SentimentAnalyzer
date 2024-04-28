from django.contrib import admin
from django.urls import path,include
from .import views

app_name='Community'

urlpatterns = [
    path('postComment', views.CommPostComment, name='CommPostComment'),
    path('', views.CommHome, name='CommHome'),
    path('<str:slug>', views.CommPost, name='CommPost'),
]