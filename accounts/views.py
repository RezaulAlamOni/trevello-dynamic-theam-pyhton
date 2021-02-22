from django.shortcuts import render


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        pwd2 = request.POST['pwd2']
    else:
        return render(request, 'accounts/register.html')
