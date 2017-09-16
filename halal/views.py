from django.shortcuts import render
import urllib
import os
from colorthief import ColorThief
import PIL
from PIL import Image


def home(request):
    results = "Submit a photo above to certify your food/drink. Please submit only high-res images for accuracy."
    return render(request, 'index.html', {"results": results})


def process_image(request):
    url = request.FILES.get('imgBase64')
    print(url)

    results = dominant_color_from_url(url)
    result = ((results[1]*1.00)/256)*100
    return render(request, 'index.html', {"results": result})
    # except:
    #     results = "Submit a photo above to certify your food/drink. Please submit only high-res images for accuracy."
    #     return render(request, 'index.html', {"results": results})

def dominant_color_from_url(url):
    '''Downloads ths image file and analyzes the dominant color'''
    color_thief = ColorThief(url)
    dominant_color = color_thief.get_color(quality=40)
    return dominant_color