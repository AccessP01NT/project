from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from django.contrib import messages

def homePage(request):
    return render(request,'loginPage/login.html',{}) 
    
def submit_login(request):
    # כפתור התחברות אחרי שהכנסנו נתונים
    userName=request.POST.get('username', None)
    password=request.POST.get('password', None)
    user=User.objects.filter(userName=userName).filter(password=password)
    if not user:
        return render(request,'loginPage/login.html',{})
    global now_user
    now_user=user[0]
    return render(request,f'users/{user[0].role}.html',{'user':(user[0])}) 

def returnOverview(request):
    return render(request,f'users/{now_user.role}.html',{'user':(now_user)}) 

def submit_registration(request):
    #כפתור הרשמה אחרי שמלאנו פרטים 
    user=User()
    user.firstName=request.POST['firstName']
    user.lastName=request.POST['lastName']
    user.userName=request.POST['userName']
    user.password=request.POST['password']
    user.role=request.POST['role']
    userTest=User.objects.filter(userName=user.userName)
    if userTest :
        #הודעה שהשם משתמש כבר תפוס
        messages.success(request, 'User Already In Registered')
        return render(request,'registerPage/register.html',{})
    user.save()
    return render(request,'loginPage/login.html',{}) 
def setNowUser(user):
    global now_user
    now_user=user
def getNowUser():
    return now_user
def isName(str):
    return str.isalpha()
def isRole(str):
    return not (str=="Choose role")
def isUserName(str):
    return str[:1].isalpha()

# Create your views here.
