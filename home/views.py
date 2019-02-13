from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django !')
    
def dinner(request):
    menus = ['chicken', 'shakeshack', 'inandout']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus':menus, 'pick':pick})