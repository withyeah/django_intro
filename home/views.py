from django.shortcuts import render, HttpResponse
import random
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse('Welcome to Django !')
    return render(request, 'home/index.html')
    
def dinner(request):
    menus = ['chicken', 'shakeshack', 'inandout']
    pick = random.choice(menus)
    return render(request, 'home/dinner.html', {'menus':menus, 'pick':pick})
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})
    
def cube(request, num):
    cubenum = int(num)**3
    return render(request, 'home/cube.html', {'num':num, 'cubenum':cubenum})
    
def ping(request):
    return render(request, 'home/ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'home/pong.html', {'data':data})
    
def user_new(request):
    return render(request, 'home/user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'home/user_create.html', {'nickname':nickname, 'pwd':pwd})
    
def template_example(request):
    my_list = ['pasta', 'pizza', 'steak', 'taco']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'home/template_example.html', 
                {'my_list': my_list, 'my_sentence': my_sentence,
                    'messages': messages, 'empty_list': empty_list,
                    'datetimenow': datetimenow
                })
                
def static_example(request):
    return render(request, 'home/static_example.html')