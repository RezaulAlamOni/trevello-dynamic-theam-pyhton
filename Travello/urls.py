from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('blog',views.blogs, name='blogs'),
    path('single-blog',views.single_blog, name='single-blog'),
    path('contact',views.contact, name='contact'),
    path('travel_destination',views.travel_destination, name='travel_destination'),
    path('destination_details',views.destination_details, name='destination_details'),
];
