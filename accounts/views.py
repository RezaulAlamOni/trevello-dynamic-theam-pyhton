from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        pwd2 = request.POST['pwd2']

        if pwd == pwd2:
            if User.objects.filter(username=username).exists():
                print('User already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=f_name, last_name=l_name, email=email,                               password=pwd)
                user.save()
                print('User Create user')
        else:
            print('Password not match')
            return redirect('register')

        return redirect('/');
    else:
        return render(request, 'accounts/register.html')
