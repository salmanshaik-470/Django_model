from django.shortcuts import render
from app1.forms import *

# Create your views here.
def home(request):
    fm=Salman()
    return render(request,'home.html',{'f':fm})