from django.shortcuts import render

def home(request):
    return render(request, "portfolio/home.html")

def cases(request):
    return render(request, "portfolio/cases.html")

def investigations(request):
    return render(request, "portfolio/investigations.html")
