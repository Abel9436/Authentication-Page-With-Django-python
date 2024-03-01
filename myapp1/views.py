from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    

    return render(request,'auth/index.html')
def signin(request):
    fname=''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('logged in')
            login(request, user)
            messages.success(request, f'Welcome, {fname}!')
            fname = user.first_name
            return render(request,'auth/home.html',{'fname':fname})
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'auth/signin.html')
def signup(request):
    
    if request.method=='POST':
        username=request.POST['username']
        fullname=request.POST['fullname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            user=User.objects.create_user(username,email,password)
            user.first_name=fullname
            user.save()
            messages.success(request,'Successfully Signed up')
            return redirect('signin')
    return render(request,'auth/signup.html')
def homepage(request):
    return render(request,'auth/home.html')