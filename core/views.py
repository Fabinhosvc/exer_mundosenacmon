from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def home(request):
    return render(request, 'main/home.html')

@login_required
def profile(request):
    context = {'berries': 150}
    return render(request, 'main/profile.html', context)

def about(request):
    return render(request, 'main/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
