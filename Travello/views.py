from django.shortcuts import render;
from django.http import HttpResponse;

# Create your views here.
from Travello.models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = 'Italy'
    dest1.places = '2'
    dest1.price = 500
    dest1.img = '1.png'
    dest2 = Destination()
    dest2.name = 'Brazil'
    dest2.places = '7'
    dest2.price = 500
    dest2.img = '2.png'
    dest3 = Destination()
    dest3.name = 'America'
    dest3.places = '2'
    dest3.price = 500
    dest3.img = '3.png'
    dest4 = Destination()
    dest4.name = 'Nepal'
    dest4.places = '5'
    dest4.price = 500
    dest4.img = '4.png'
    dest5 = Destination()
    dest5.name = 'Maldives'
    dest5.places = '2'
    dest5.price = 500
    dest5.img = '5.png'
    dest6 = Destination()
    dest6.name = 'Indonesia'
    dest6.places = '10'
    dest6.price = 500
    dest6.img = '6.png'
    dests = [dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request, 'index.html',{'dests' : dests});

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


