from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':                # ako je pokrenuta registracija
        form = UserCreationForm(request.POST)   # spremi sve u form
        if form.is_valid():                     # provjeri spremljene podatke
            username = form.cleaned_data.get('username')    # ako je sve ispravno, pokupi s forme upisani username
            messages.success(request, f'Account created for {username}!')   # javi poruku, f je fsting format
            return redirect('blog-home')        # redirect nas vraća na zadanu stranicu
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})