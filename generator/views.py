from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse('Hello there Friend!')
    return render(request,'generator_app/home.html', {'password':'huiyrf456789'})  #dictionary is the parameter passed

    #render - handles the request and return the template in an html
    

def password(request):
    #return HttpResponse("<h1>Eggs are so tasty<h1>")
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
       characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
       characters.extend(list('0123456789'))

    if request.GET.get('special'):
       characters.extend(list('#$@%^&*~![]()')) 

    length = int(request.GET.get('length', 12)) # 12 is like a default value

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator_app/password.html', {'password':thepassword})


def aboutus(request):
    return render(request, 'generator_app/aboutus.html')