from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

def root(request):
    return HttpResponseRedirect('home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')

def home_page(request):
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def portfolio_page(request):
        image_urls = []
        for i in range(5):
                random_number = randint(0, 100)
                image_urls.append("https://picsum.photos/200/200?imahe={}".format(random_number))
        context = {'gallery_images': image_urls}
        response = render(request, 'gallery.html', context)
        return HttpResponse(response)


def about_me(request):
    context = {'skills': ['HTML', 'CSS', 'Python'], 'interests': ['Coding', 'Basketball', 'Adventures']}
    response = render(request, 'about.html', context)
    return HttpResponse(response)


def favourites_page(request):
    context = {'fave_link': "https://www.youtube.com/"}
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)
