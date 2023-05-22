from django.shortcuts import render

def home(request):
    return render(request, "frontPage/home.html")

def about(request):
    return render(request, "frontPage/about.html")

def contact(request):
    return render(request, "frontPage/contact.html")