from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request): #Главная страница
    return HttpResponse('Страница Запросника')
  #  if request.POST: #Ввод запроса
  #      print(request.POST)
  #      return redirect('zapros') #Возрат при неверном вводе

def news(request): #Страница новостей
    return HttpResponse('<h1>Новости электронники</h1>')

def answer(request, stok):#Страница ответа запросника
   return HttpResponse(f'<h1>Ответ</h1><p>{stok}</p>')
   # if request.POST:  # Ввод запроса
   #     print(request.POST)
   #     return redirect('zapros')  # Возрат при неверном вводе

def pageNotFound(request, exception):#Страница 404
    return HttpResponseNotFound('<h>Страница не найдена</h>')

def office(request): #Главная страница
    return HttpResponse('Личный кабинет')

