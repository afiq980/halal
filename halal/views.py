from django.shortcuts import render
import urllib
import os
from colorthief import ColorThief


def home(request):
    return render(request, 'index.html', {})


def process_image(request):
    url = request.FILES.get('imgBase64')
    results = dominant_color_from_url(url)[1]
    return render(request, 'index.html', {"results": results})


def dominant_color_from_url(url):
    '''Downloads ths image file and analyzes the dominant color'''
    color_thief = ColorThief(url)
    dominant_color = color_thief.get_color(quality=1)
    return dominant_color