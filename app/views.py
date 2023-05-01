from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *


def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)     
        if SFDO.is_valid():
            sid=SFDO.cleaned_data['sid']
            sname=SFDO.cleaned_data['sname']
            email=SFDO.cleaned_data['email']
            SD=Student.objects.get_or_create(sid=sid,sname=sname,email=email)[0]
            SD.save()


            SQS=Student.objects.all()
            d1={'SQS':SQS}
        
        return render(request,'displaystudent.html',d1)



    return render(request,'student.html',d)
