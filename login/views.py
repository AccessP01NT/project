from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
new_user=None
def homePage(request):
    return render(request,'loginPage/login.html',{})
    
def adminpage():
 assert isinstance(request,HttpRequest)     
 List_user=tutor.objects.all()
 return render(request,'login/users/admin.html'  ,{'List_user':List_user}) 

def submit_login(request):
    # כפתור התחברות אחרי שהכנסנו נתונים
    userName=request.POST.get('username', None)
    password=request.POST.get('password', None)
   
    user=User.objects.filter(userName=userName).filter(password=password)
    if not user:
        return render(request,'loginPage/login.html',{})
    return render(request,f'users/{user[0].role}.html',{'user':(user[0])})
     
def submit_registration(request):
    #כפתור הרשמה אחרי שמלאנו פרטים 
    user=User()
   
    user.firstName=request.POST['firstName']
    user.lastName=request.POST['lastName']
    user.userName=request.POST['userName']
    user.password=request.POST['password']
    print(user.firstName)
    user.role=request.POST['role']
    user.save()
    return render(request,'loginPage/login.html',{}) 

def isName(str):
    return str.isalpha()
def isRole(str):
    return not (str=="Choose role")
def isUserName(str):
    return str[:1].isalpha()

# Create your views here.
