from django.shortcuts import render,HttpResponse
from .models import User
from .forms import *
# Create your views here.
def show_user(request):
    user=User.objects.all()
    context={'user':user}
    return render (request,'admin_temp/user.html',context)
def show_profile(request,id):
  user=User.objects.get(id=id)
  context={'id': user.id,'name':user.username,'email':user.email,'password':user.password}
  return render (request,'admin_temp/profile.html',context)

def add_product(request): 
  if request.method == "POST":
     form = AddProduct(request.POST)
     if form.is_valid():
        form.save()
        return HttpResponse ('Done')

  form = AddProduct() 
  context = {'form':form}
  return render (request,'admin_temp/add_product.html',context)

def add_user(request):
  if request.method == "POST":
     form = AddUser(request.POST)
     if form.is_valid():
        form.save()
        return HttpResponse ('Done')
  form=AddUser()
  context={'form':form}
  return render (request,'admin_temp/add_user.html',context)