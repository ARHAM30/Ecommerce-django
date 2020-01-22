from django.shortcuts import render
from .forms import usercreate

def register(request):
    f=usercreate()
    return render(request,'resgister.html',{'f':f})


