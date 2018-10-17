from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Mario',
        'title': 'Naslov 1. bloga',
        'content': 'Tekst bloga',
        'date_posted': 'Listopad 17, 2018'
    },
    {
        'author': 'Marija',
        'title': 'Naslov 2. bloga',
        'content': 'Tekst bloga',
        'date_posted': 'Listopad 18, 2018'
    }
]

def home(request):
    '''
    Logika za rutu kojom korisnik vidi stranicu
    :param request:
    :return: vraća render template stranice koju želim, prvi argument je obavezno request, a drugi je ruta do template-a
    '''
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})