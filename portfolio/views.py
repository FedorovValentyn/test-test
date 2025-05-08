from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'portfolio/index.html', {'projects': projects})

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactRequest.objects.create(name=name, email=email, message=message)
    return render(request, 'portfolio/contact.html')