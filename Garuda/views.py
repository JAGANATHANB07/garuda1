from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"Garuda/home.html")

def about(request):
    return render(request,"Garuda/about.html")

def contact(request):
    return render(request,"Garuda/contact.html")

def projects(request):
    return render(request,"Garuda/projects.html")

