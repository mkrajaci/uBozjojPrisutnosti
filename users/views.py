from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':                # ako je pokrenuta registracija
        form = UserRegisterForm(request.POST)   # spremi sve u form
        if form.is_valid():                     # provjeri spremljene podatke
            form.save()                         # ovo sprema podatke o useru, sve od username, lozinke, mail itd.
            username = form.cleaned_data.get('username')    # ako je sve ispravno, pokupi s forme upisani username
            messages.success(request, f'Your account has been created! Now you are able to log in.')   # javi poruku, f je fsting format
            return redirect('login')        # redirect nas vraća na zadanu stranicu
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')