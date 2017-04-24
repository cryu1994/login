from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
def index(request):
    return render(request, "index/index.html")
def register(request):
    postData = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'conf_password': request.POST['conf_password']
    }
    errors = User.objects.register(postData)
    for error in errors:
        messages.error(request, error)


    if not errors:
        user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = request.POST['password'])
        request.session['user_id'] = user.id
        request.session['name'] = user.first_name
        return redirect('/success')

    request.session['loginError']=False
    return redirect('/')

def login(request):
    loginData = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    errors = User.objects.login(loginData)

    for error in errors:
        messages.error(request, error)

    if not errors:
        user = User.objects.verify(loginData)
        return redirect('/success')

    request.session['loginError']=True

    return redirect('/')

def success(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, "index/success.html", context)
def logout(request):
    return redirect('/')

# Create your views here.
