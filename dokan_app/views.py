from django.shortcuts import render,HttpResponse
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from .models import Dokan
# Create your views here.

@login_required(login_url='/login')
def show_dokan(request):
    dokan=Dokan.objects.all()
    context={'dokan':dokan}
    return render (request,'admin_temp/dokan.html',context)

def user_create(request):
    if request.method =='POST':
        form= UserForm(request.POST)
        password= request.POST.get('password')
        username= request.POST.get('username')
        if form.is_valid():
            user= User.objects.create_user(username=username,password=password)
            return HttpResponse ('Done')

    form= UserForm()
    context={'form':form}
    return render (request,'admin_temp/registration.html',context)

def user_login(request):
    if request.method =='POST':
        form= UserForm(request.POST)
        password= request.POST.get('password')
        username= request.POST.get('username')
        user= authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            form= UserForm()
            context={'username':username}
            return render (request,'admin_temp/dash.html',context)
        else:
            form= UserForm()
            context={'msg':"You User & Password is Worng",'form':form}
            return render (request,'admin_temp/login.html',context)


    form= UserForm()
    context={'form':form}
    return render (request,'admin_temp/login.html',context)


def user_logout(request):
    logout(request)
    return HttpResponse("Logout")
    

   # dokan=Dokan.objects.all()
   # context={'dokan':dokan}
   

