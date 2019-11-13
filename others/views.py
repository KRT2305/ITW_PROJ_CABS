from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from kuber.models import revs
# Create your views here.
def about(request):
    revw = revs.objects.all()
    return render(request,'about.html',{'revw':revw})
def service(request):
    return render(request,'service.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')