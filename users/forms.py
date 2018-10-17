from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):   # UserRegistarionForm nasljedjuje UserCreationForm
    email = forms.EmailField()              # dodajem polje koje zelim, naziv = tip polja i ovdje mogu stavljati arbumente default itd

    class Meta:
        model = User    # ovime formi govorim s kojim modelom da komunicira
        fields = ['username', 'email', 'password1', 'password2']    # polja koja ce biti prikazana na formi i njihov redoslijed