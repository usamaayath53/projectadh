from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from.forms import newappForm
from.models import newApplication

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
            return render(request,'userdashboard.html')
        else:
            msg="Invalid credentials"
    
    return render(request,'login.html',{'msg':msg})

@login_required
def userlogout(request):
    logout(request)
    return redirect('login')
        
@login_required
def userdashboard(request):
    msg="Welcome Admin"
    return render(request,'userdashboard.html',{'msg':msg})

@login_required
def newapplication(request):
    frm=newappForm()
    msg=None
    if request.POST:
        frm=newappForm(request.POST)
        if frm.is_valid:
            frm.save()
            msg="New Application added"
            frm=newappForm()
            return render(request,'newapplication.html',{'frm':frm,'msg':msg})
        else:
            frm=newappForm()
            msg="Something went wrong"
        # print(frm)
    return render(request,'newapplication.html',{'frm':frm,'msg':msg})

@login_required
def viewapplication(request):
    frm=newApplication.objects.all()
    return render(request,'viewapp.html',{'frm':frm})

@login_required
def search(request):
    msg=None
    num=None
    # data=None
    if request.POST:
        name=request.POST['searchbox'].strip()
        data_exists=newApplication.objects.filter(Name=name).exists()
        # print(data_exists)
        if data_exists:
            data=newApplication.objects.filter(Name=name)
            num=len(data)
            msg= f"{num} results found"
        else:
            data=newApplication.objects.none()
            msg="No details found"
    print(data)
    return render(request,'editview.html',{'frm':data, 'msg':msg})

@login_required
def quicklinks(request):
    return render(request,'links.html')

@login_required
def editsearch(request):
    msg=None
    num=None
    # data=None
    if request.POST:
        name=request.POST['searchbox'].strip()
        data_exists=newApplication.objects.filter(Name=name).exists()
        # print(data_exists)
        if data_exists:
            data=newApplication.objects.filter(Name=name)
            num=len(data)
            msg= f"{num} results found"
        else:
            data=newApplication.objects.none()
            msg="No details found"
    print(data)
    return render(request,'viewapp.html',{'frm':data, 'msg':msg})

@login_required
def editview(request):
    msg=None
    allobj=newApplication.objects.all()
    return render(request,'editview.html',{'frm':allobj})

@login_required
def editapp(request,pk):
    obj=newApplication.objects.get(id=pk)
    frm=newappForm(instance=obj)
    if request.POST:
        frm=newappForm(request.POST, instance=obj)
        if frm.is_valid:
            frm.save()
            frm=newApplication.objects.all()
            msg="Changes updated Successfully"
            return render(request,'editview.html',{'frm':frm,'msg':msg})
    return render(request,'newapplication.html',{'frm':frm})





