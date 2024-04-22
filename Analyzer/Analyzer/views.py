from django.shortcuts import render,redirect,HttpResponse
from SentimentAnalysis.models import comment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

def index(request):
  return render(request, 'index.html')

def GetHistory(request):
  comm = comment.objects.filter(user = request.user)
  return render(request, 'history.html', {'comments':comm})

def HandleSignup(request):
    if request.method == 'POST':
        # Getting Post parameters...
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for erroneous inputs...
        if len(username) > 12:
            messages.warning(request, "Username must be under 12 characters !!!")
            return redirect('index')
        
        if not username.isalnum():
            messages.warning(request, "Username should only contain letters and numbers !!!")
            return redirect('index')

        if pass1 != pass2:
            messages.warning(request, "Passwords do not match")
            return redirect('index')
        # Creating New user...
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been Successfully created...")
        return redirect('index')
    else:
        return HttpResponse('404 - Not Found') 

def HandleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully LoggedIn...")
            return redirect('index')
        else:
            messages.error(request, "Invalid Login Credentials...")
            return redirect('index')

def HandleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out...")
    return redirect('index')