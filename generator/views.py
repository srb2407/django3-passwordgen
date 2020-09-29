from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, r'generator\home.html')


def about(request):
    return render(request, r'generator\about.html')


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('UpperCase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Special'):
        chars.extend(list('@#%&()!*$?'))

    if request.GET.get('Numbers'):
        chars.extend(list('0123456789'))

    thepassword = ''

    length = int(request.GET.get('length', 8))

    for _ in range(length):
        thepassword += random.choice(chars)

    return render(request, r'generator\password.html', {'password': thepassword})
