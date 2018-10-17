from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    '''
    Logika za rutu kojom korisnik vidi stranicu
    :param request:
    :return: vraća render template stranice koju želim, prvi argument je obavezno request, a drugi je ruta do template-a
    '''
    context = {
        'posts': Post.objects.all()     # query koji dohvaća podatke iz baze
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})