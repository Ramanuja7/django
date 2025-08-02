from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate,logout
def home(request):

    #return HttpResponse("hello , this is the home page of my app")
    return render(request,'home.html')
def about(request):
    return render(request,"about.html")
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

