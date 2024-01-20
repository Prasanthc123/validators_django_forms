from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *

def schoolform(request):
    ESFO=Schoolform()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sp=SFDO.cleaned_data['sprincipal']
            sl=SFDO.cleaned_data['slocation']
            se=SFDO.cleaned_data['semail']
            re=SFDO.cleaned_data['remail']
            SO=School.objects.get_or_create(sname=sn,sprincipal=sp,slocation=sl,semail=se,remail=re)[0]
            SO.save()

            QLSO=School.objects.all()
            d1={'School':QLSO}
            return render(request,'display_school.html',d1)
    return render(request,'createschool.html',d)

