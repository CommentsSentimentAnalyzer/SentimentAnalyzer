from django.shortcuts import render,redirect
from .models import comment
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Create your views here.
def SentimentHome(request):
    return render(request,'Sentimentanalysis/home.html')

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize the Sentiment Intensity Analyzer
sid = SentimentIntensityAnalyzer()

def make_prediction(text):
  sentiment_scores=sid.polarity_scores(text)
  if sentiment_scores['pos'] > sentiment_scores['neg'] and sentiment_scores['pos'] > sentiment_scores['neu'] :
    sentiment = "Positive"
  elif sentiment_scores['neg'] > sentiment_scores['neu'] and sentiment_scores['neg'] > sentiment_scores['pos']:
    sentiment = "Negative"
  else:
    sentiment = "Neutral"
  return sentiment

# user_input=input("Input Prompt:")
# result=make_prediction(user_input)
# print("Answer: ",result)

def formresult(request):
  if request.method == 'POST':
    c = request.POST.get('comment')
    commentRes = make_prediction(c)
    comm = comment()
    comm.comment = c
    comm.user = request.user
    comm.result = commentRes
    comm.save()
    return render(request,'Sentimentanalysis/home.html',{'comment':commentRes})
