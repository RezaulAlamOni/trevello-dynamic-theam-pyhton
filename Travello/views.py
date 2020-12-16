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
    return render(request, 'about.html');


