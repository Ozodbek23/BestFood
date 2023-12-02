from django.contrib.auth.decorators import login_required as _login_required
from django.contrib.auth import authenticate, login as _login , logout as _logout
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator


def login_required(func):
    return _login_required(func , login_url='login')

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            _login(request , user)
            return redirect('/')

    return render(request,'login.html')

@login_required
def logout(request):
    _logout(request)
    return redirect('login')


