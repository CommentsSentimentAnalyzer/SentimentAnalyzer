from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    # path('postComment', views.CommPostComment, name='CommPostComment'),
    path('', views.SentimentHome, name='SentimentHome'),
    # path('<str:slug>', views.CommPost, name='CommPost'),
]