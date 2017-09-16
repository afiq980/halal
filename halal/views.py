from django.shortcuts import render
import urllib
import os
from colorthief import ColorThief


def home(request):
    return render(request, 'index.html', {})


def process_image(request):
    url = request.FILES.get('imgBase64')
    print(dominant_color_from_url(url))
    return render(request, 'index.html', {})


def dominant_color_from_url(url,tmp_file='tmp.jpg'):
    '''Downloads ths image file and analyzes the dominant color'''
    urllib.urlretrieve(url, tmp_file)
    color_thief = ColorThief(tmp_file)
    dominant_color = color_thief.get_color(quality=1)
    os.remove(tmp_file)
    return dominant_color