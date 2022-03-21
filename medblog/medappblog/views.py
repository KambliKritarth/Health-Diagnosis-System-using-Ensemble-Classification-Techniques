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


def submitmyform(request):
    
    model = Score
    all_scores = Score.objects.all
    
    #print(mydictionary["name"]), name = mydictionary["name"], lastname = mydictionary["lastname"],
    result =getPredictions(request.POST.get('Tenthmarks',0) , request.POST.get('Twelfthmarks',0), request.POST.get('Gender',0) , request.POST.get('Sports',0) ,request.POST.get('Indo',0) , request.POST.get('Danc',0), request.POST.get('Teach',0), request.POST.get('Art',0), request.POST.get('Sing',0), request.POST.get('WestClass',0), request.POST.get('Fest',0), request.POST.get('Speech',0), request.POST.get('Gam',0), request.POST.get('Strict',0), request.POST.get('ClassR',0),request.POST.get('Pers',0), request.POST.get('Oly',0), request.POST.get('OlyMar',0), request.POST.get('Head',0))
    sample_set = {"Software Engineer", "Investment Banker", "Consultant", "Product Designer","Financial Accountant","Bank Engineer","Jr. College Professor","Physiotherapist","Civil Engineer","Architect","Orthodontist","Sales Manager"}
   
    ins = Score( result, DataBaseF, CA, DCS, Net, SoftWD, ProgSkills, AIML, SWE, BusinessAnalysis, DataScience, GraphDesign)

    ins.save()
    print(result)
    return render(request,'submitmyform.html',{'submitmyform':result})