from django.shortcuts import render
import joblib
# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def greet(request,name):
    return render(request,"hello/greet.html",{
        "icon":name.capitalize()
    })

def result(request):
    cls = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['FA'])
    lis.append(request.GET['VA'])
    lis.append(request.GET['CA'])
    lis.append(request.GET['RS'])
    lis.append(request.GET['C'])
    lis.append(request.GET['FSD'])
    lis.append(request.GET['TSD'])
    lis.append(request.GET['D'])
    lis.append(request.GET['PH'])
    lis.append(request.GET['S'])
    lis.append(request.GET['A'])

    # print(lis)
    ans = cls.predict([lis])

    return render(request,"hello/result.html",{
        "ans":ans
    })