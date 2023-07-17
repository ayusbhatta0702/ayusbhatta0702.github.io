from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Ayus Bhattacharya',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts,
        #'title': 'Home'
    }
    #return render(request, 'path to template file', dictionary for extra information)
    return render(request, 'Mahiblog/home.html', context)

def about(request):
    return render(request, 'Mahiblog/about.html', {'title': 'About'})