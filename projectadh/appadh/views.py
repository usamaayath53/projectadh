from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request,'home.html')


def userlogin(request):
    user=None
    msg=None
    if request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect(userdashboard)
        else:
            msg="Invalid credentials"
            print("abc")
    return render(request,'login.html',{'msg':msg})
        
@login_required
def userdashboard(request):
    msg="Welcome Admin"
    return render(request,'userdashboard.html',{'msg':msg})



