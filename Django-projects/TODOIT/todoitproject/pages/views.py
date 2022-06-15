from django.shortcuts import render
import requests

# Create your views here.
def index(request): 
    context = {} 
    return render(request, 'pages/index.html', context=context)

def edit(request): 
    context = {} 
    return render(request, 'pages/edit.html', context=context)

# BASE_URL = 'https://jsonplaceholder.typicode.com' # Базовый URL
# users_url = '/users' # 10 пользователей


# def hw_users(request): 
#     # session = requests.Session()
#     req = requests.get(BASE_URL + users_url)
#     data = req.json()
#     context = {'users': data}
#     return render(request, 'pages/random_users.html', context=context)