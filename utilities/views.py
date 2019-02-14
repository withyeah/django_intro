from django.shortcuts import render
from datetime import datetime
import requests, os


# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

def bye(request):
    dday = datetime.strptime('2019-02-28', '%Y-%m-%d')
    now = datetime.now()
    left = dday - now
    return render(request, 'utilities/bye.html', {'left':left})

def graduation(request):
    dday = datetime.strptime('2019-05-28', '%Y-%m-%d')
    now = datetime.now()
    left = dday - now
    return render(request, 'utilities/graduation.html', {'left':left})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    key = os.getenv('WEATHER_TOKEN')
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID={key}'
    req = requests.get(url).json()
    weather = req['weather'][0]['description']
    now = datetime.now()
    return render(request, 'utilities/today.html', {'weather':weather, 'now':now})

def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')

def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    ascii_art = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'ascii_art':ascii_art})
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    naver_client_id = os.getenv('NAVER_CLIENT_ID')
    naver_client_secret = os.getenv('NAVER_CLIENT_SECRET')
    text = request.GET.get('text')
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": text
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    return render(request, 'utilities/translated.html', {'reply_text': reply_text})