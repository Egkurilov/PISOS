from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from Admin.models import Settings, Task, TaskType


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


class TaskTypeAddView(View):
    def get(self, request):
        if 'is_admin' in request.session:
            exists_task_type = TaskType.objects.values()
            return render(request, 'admin/TaskTypeAdd.html',  context={'exists_task_type': exists_task_type})
        return render(request, 'admin/Login.html')

    def post(self, request):
        task_type = request.POST.get('task_type')
        description = request.POST.get('description')
        if task_type:
            TaskType.objects.create(name=task_type, description=description)

            return render(request, 'admin/Dashboard.html')
        return redirect('/admin/dashboard')


class TaskAddView(View):
    def get(self, request):
        if 'is_admin' in request.session:
            exists_task_type = TaskType.objects.values()
            exists_task = Task.objects.values()

            return render(request, 'admin/TaskAdd.html', context={'task_type': exists_task_type, 'exists_task': exists_task})
        return render(request, 'admin/Login.html')

    def post(self, request):

        task_type = request.POST.get('task_type')
        task_name = request.POST.get('task_name')
        enable_box = request.POST.get('enable-box')

        print(request.POST)
        if task_name:
            Task.objects.create(name=task_name, task_type_id=task_type, enable=enable_box)
            return render(request, 'admin/Dashboard.html')
        return redirect('/admin/dashboard')

