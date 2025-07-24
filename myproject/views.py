from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("hello , this is the home page of my app")
    return render(request,'home.html')
def about(request):
    return render(request,"about.html")
