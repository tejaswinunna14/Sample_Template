from django.shortcuts import render

from django.http import HttpResponse
def songs(request):
    return HttpResponse('<h1>I like Listening songs</h1>')