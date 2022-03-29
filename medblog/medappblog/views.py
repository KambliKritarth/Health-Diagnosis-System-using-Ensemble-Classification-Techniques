from django.shortcuts import render
from medappblog.models import HDSymptom
import pickle

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def covid(request):
    return render(request,'COVID19.html',{})

def heartdisease(request):
    return render(request,'heartdisease.html',{})

def diabetes(request):
    return render(request,'diabetes.html',{})

def getPredictions(age, anaemia, CreatiPhosph, anaemia, EjectFract, highBP, SerCreat, SerSodiu, sex, smoking, followUpTime):
    
    model = pickle.load(open("careerguide.sav","rb"))
    scaled = pickle.load(open("careerguidescaler.sav","rb"))
    prediction = model.predict(scaled.transform([age, anaemia, CreatiPhosph, anaemia, EjectFract, highBP, SerCreat, SerSodiu, sex, smoking, followUpTime]))
    return prediction

def submitmyform(request):
    
    model = HDSymptom
    all_scores = HDSymptom.objects.all
    
    #print(mydictionary["name"]), name = mydictionary["name"], lastname = mydictionary["lastname"],
    result =getPredictions(request.POST.get('age',0) , request.POST.get('anaemia',0), request.POST.get('EjectFract',0) , request.POST.get('highBP',0) ,request.POST.get('SerCreat',0) , request.POST.get('SerSodiu',0), request.POST.get('sex',0), request.POST.get('smoking',0), request.POST.get('Sing',0), request.POST.get('followUpTime',0))
   
    ins = HDSymptom( result,age, anaemia, CreatiPhosph, anaemia, EjectFract, highBP, SerCreat, SerSodiu, sex, smoking, followUpTime )

    ins.save()
    #print(result)
    return render(request,'submitmyform.html',{'submitmyform':result})