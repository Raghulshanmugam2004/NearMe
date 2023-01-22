
from django.shortcuts import render
def map(request):
    return render(request,'newapp/map.html')
def court(request):
    return render(request,'newapp/court.html')   
def hospital(request):
    return render(request,'newapp/hospital.html')  
def park(request):
    return render(request,'newapp/park.html')  
def railway(request):
    return render(request,'newapp/railway.html')  
def theatre(request):
    return render(request,'newapp/theatre.html')                  
