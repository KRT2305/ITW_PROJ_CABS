from django.shortcuts import render,redirect
from .models import revs,reservations
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    if request.method=='POST':
        phone=request.POST['phone']
        date=request.POST['date']
        origin=request.POST['origin']
        destination=request.POST['destination']
        time=request.POST['time']
        user= str(request.user)
        k = reservations.objects.create(user=user,phone=phone,date=date,time=time)
        
        return redirect('/')
    else:
        revw= revs.objects.all()
        return render(request,'index.html',{'revw' : revw})