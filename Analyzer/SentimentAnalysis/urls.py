from django.contrib import admin
from django.urls import path,include
from .import views

app_name='SentimentAnalysis'

urlpatterns = [
    # path('postComment', views.CommPostComment, name='CommPostComment'),
    path('', views.SentimentHome, name='SentimentHome'),
    path('sentimentResult/' , views.formresult,name="formresult")
]