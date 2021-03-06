import re

from django.shortcuts import render, redirect
from django.views import View


from Auth.models import User


class LoginView(View):
    def get(self, request):
        if '001' in request.session:
            return render(request, 'square/Square.html')
        return render(request, 'auth/login.html')

    def post(self, request):
        login = request.POST.get('login')
        password = request.POST.get('password')

        if login and password:
            login = re.match(r'[а-яА-Яa-zA-Z0-9]*', login)
            password = re.match(r'[а-яА-Яa-zA-Z0-9]*', password)
        if login.group(0) and password.group(0):
            if not User.objects.values().filter(user_login=login.group(0)):
                return render(request, 'auth/registration.html', context={'error': 'Пользователя не существует'})
            request.session['permission'] = '001'
            return redirect('/cp')


class RegisterView(View):
    def get(self, request):
        if 'is_admin' in request.session:
            return redirect('/')
        return render(request, 'auth/registration.html')

    def post(self, request):
        login = request.POST.get('login')
        password = request.POST.get('password')
        if login and password:
            login = re.match(r'[а-яА-Яa-zA-Z0-9]*', login)
            password = re.match(r'[а-яА-Яa-zA-Z0-9]*', password)
        if login.group(0) and password.group(0):
            if User.objects.values().filter(user_login=login.group(0)):
                return render(request, 'auth/registration.html', context={'error': 'пользователь существует'})
            User.objects.create(user_login=login.group(0), password=password.group(0), permission='001')
            request.session['login'] = login.group(0)
            request.session['permission'] = '1'
            return redirect('/login')
        return render(request, 'auth/registration.html')