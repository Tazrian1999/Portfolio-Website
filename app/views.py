from django.shortcuts import render
from .models import Profile

# Create your views here.
def index(request):
    profile = Profile.objects.all()
    return render(request,'index.html',{'profile':profile})

def contact(request):
    return render(request,'contact.html')


def projects(request):
    return render(request,'projects.html')


def resume(request):
    return render(request,'resume.html')