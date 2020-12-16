from django.shortcuts import render;
from django.http import HttpResponse;

# Create your views here.

def index(request):
    return render(request, 'index.html',{'name' : "Rezaul Alam Zilani"});

def about(request):
    return render(request, 'about.html');

def blogs(request):
    return render(request, 'blog.html');

def single_blog(request):
    return render(request, 'single-blog.html');

def contact(request):
    return render(request, 'contact.html');

def travel_destination(request):
    return render(request, 'travel_destination.html');

def destination_details(request):
    return render(request, 'destination_details.html');


