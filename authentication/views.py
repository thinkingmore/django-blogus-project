from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm


# sign up user with email and password

def user_signup(request):    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

# login user with email and password

def user_signin(request):
    if request.user.is_authenticated:
        return redirect('/')
      
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})
    
def user_logout(request):
    logout(request)
    return redirect('/auth/login')

