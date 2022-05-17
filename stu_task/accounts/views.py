
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def register(req):
    form = UserRegisterForm()
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        context = {'data' : request.POST}
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email,password=password)
   
        login(request,user)
        # messages.add_message(request,messages.SUCCESS,f'Welcome{user.username}')
        return redirect(reverse('home'))

    return render(request,'accounts/login.html')

@login_required()
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return HttpResponse("<h1>Home</h1>")