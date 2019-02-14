from django.shortcuts import render, HttpResponse
import random
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse('Welcome to Django !')
    return render(request, 'index.html')
    
def dinner(request):
    menus = ['chicken', 'shakeshack', 'inandout']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus':menus, 'pick':pick})
    
def hello(request, name):
    return render(request, 'hello.html', {'name':name})
    
def cube(request, num):
    cubenum = int(num)**3
    return render(request, 'cube.html', {'num':num, 'cubenum':cubenum})
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data':data})
    
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname':nickname, 'pwd':pwd})
    
def template_example(request):
    my_list = ['pasta', 'pizza', 'steak', 'taco']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'template_example.html', 
                {'my_list': my_list, 'my_sentence': my_sentence,
                    'messages': messages, 'empty_list': empty_list,
                    'datetimenow': datetimenow
                })