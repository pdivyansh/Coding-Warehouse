from email import message
from django.shortcuts import render,redirect
from .models import Team,Contact
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def home(request):
    return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    teams=Team.objects.all()
    data={
        'teams':teams,
    }
    return render(request,'contact.html',data)

def course(request):
    return render(request,'course.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now loggen in.')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
       
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists!')
                    return redirect('register')
                else:
                    user=User.objects.create_user(email=email,username=username,password=password)
                    
                    user.save()
                    messages.success(request,'You are register successfully.')
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')


        messages.error(request,'this is error message')
        return redirect('register')
    else:
        return render(request,'register.html')

def course_code(request):
    return render(request,'course_code.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are successfully logged out.')
        return redirect('home')

    return redirect('home')

def contactform(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        return redirect('home')
    