from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def covid(request):
    return render(request,'COVID19.html',{})

def heartdisease(request):
    return render(request,'heartdisease.html',{})

def diabetes(request):
    return render(request,'diabetes.html',{})