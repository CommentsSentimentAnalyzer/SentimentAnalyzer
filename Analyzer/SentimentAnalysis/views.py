from django.shortcuts import render,redirect

# Create your views here.
def SentimentHome(request):
    return render(request,'SentimentAnalysis/home.html')
