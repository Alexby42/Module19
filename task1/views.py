from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import ContactForm

# Create your views here.
users = ['ab', 'cd', 'ef']
info = {}
def valid(users: list, name: str, pas: str, rep_pas: str, age: int) -> bool:
    if (name not in users) and (pas == rep_pas) and int(age) > 18:
        return True

def based(request):
    #template_name = 'sample1.html'
    return render(request, 'sample1.html')

def shop(request):
    games = []
    for game in Game.objects.all():
        games.append(game)
    context = {'games': games, }
    return render(request, 'sample2.html', context)


class basket(TemplateView):
    template_name = 'sample3.html'

def sign_up_by_django(request):
    global info
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if valid(users, username, password, repeat_password, int(age)):
                return HttpResponse(f'Приветствуем, {username}!')
            if username in users:
                info = {'error': 'Пользователь уже существует'}
            elif int(age) < 18:
                info = {'error': 'Вы должны быть старше 18'}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
    else:
        form = ContactForm()

    return render(request, 'registration_page.html', context=info)
