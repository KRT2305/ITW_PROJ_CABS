from django.shortcuts import render
from .models import revs
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    if request.method=='POST':
        phone=request.POST['phone']
        date=request.POST['date']
        origin=request.POST['origin']
        destination=request.POST['destination']
        time=request.POST['time']
        user= request.user
    else:
        revw= revs.objects.all()
        return render(request,'index.html',{'revw' : revw})