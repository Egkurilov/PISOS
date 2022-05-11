import re

from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
from Auth.models import User


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
            return render(request, 'auth/login.html')
        return render(request, 'auth/registration.html')