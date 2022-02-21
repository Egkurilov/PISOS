from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from Admin.models import Settings, Task


class DashboardView(View):
    def get(self, request):
        if 'is_admin' not in request.session:
            return redirect('/admin/login')
        task_list = Task.objects.values()
        return render(request, 'admin/Dashboard.html', context={'task_list': task_list})
    def post(self, request):
        pass


class LoginView(View):
    def get(self, request):
        if 'is_admin' in request.session:
            return redirect('/admin/dashboard')
        return render(request, 'admin/Login.html')

    def post(self, request):
        password = request.POST.get("password")
        admin_password = Settings.objects.values('value').filter(name='admin_password').first()

        if check_password(password, admin_password['value']) is not True:
            error_message = 'Ваш пароль не верен'
            return render(request, 'admin/Login.html', context={'error': error_message})

        request.session['is_admin'] = True
        return redirect('/admin/dashboard')


#https://fullcalendar.io/demos