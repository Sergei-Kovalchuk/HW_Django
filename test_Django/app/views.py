from django.shortcuts import render, reverse
from django.http import HttpResponse
import datetime
from os import listdir
def home_view(request):
    template_name = 'app/index.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}' + f'<br><a href="{reverse("home")}">Главная страница</a>'
    return HttpResponse(msg)
def workdir_view(request):
    list = listdir()
    cwd = f'Cодержимое рабочей директории: {list}' + f'<br><a href="{reverse("home")}">Главная страница</a>'
    return HttpResponse(cwd)