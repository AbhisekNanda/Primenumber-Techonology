from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import Restaurant
import json


# Create your views here.
def import_data():

    df = pd.read_csv("https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv")

    for d in df.values:

        if type(d[3]) == float:
            d[3] = json.dumps(str({"null":"null"}))
            print(d[3])

        if type(d[5]) == float:
            d[5] = json.dumps(str({"null":"null"}))
            print(d[5])

        if type(d[5]) == dict:
            d[5] = json.dumps(str(d[5]))
            print(d[5])
        
        if type(d[3]) == dict:
            d[3] = json.dumps(str(d[3]))
            print(d[3])

        Restaurant.objects.create(rest_id=d[0],rest_name=d[1],rest_location=d[2],rest_items=json.loads(d[3]),rest_lat_long=d[4],rest_full_details=json.loads(d[5]))
    
    print("added")

def home(request):

    if request.method == "POST":
        search = request.POST.get("search")
        if search == "":
            res = Restaurant.objects.all()
            context={"res":res}
            return render(request,"home.html",context=context)
        
        res = Restaurant.objects.filter(rest_items__has_key=search)
        context={"res":res}
        return render(request,"home.html",context=context)
    
    res = Restaurant.objects.all()
    context={"res":res}
    return render(request,"home.html",context=context)

def view_details(request,id):
    print(id)
    res = Restaurant.objects.filter(rest_id=id)
    print(res)
    context={"re":res[0],"items":res[0].rest_items}
    #return HttpResponse("hi")
    return render(request,"restaurant.html",context=context)
