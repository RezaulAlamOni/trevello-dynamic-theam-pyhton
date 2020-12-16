from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('blog',views.blogs, name='blogs'),
    path('single-blog',views.single_blog, name='single-blog'),
];
