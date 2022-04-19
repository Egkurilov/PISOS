import re

from django.shortcuts import render
from django.views import View

from ControlPanel.models import Category, Project


class ControlPanelView(View):
    def get(self, request):
        return render(request, 'controlpanel/mainPanel.html')


class AddCategoryView(View):
    def get(self, request):
        return render(request, 'square/AddCategory.html')

    def post(self, request):
        category_name = request.POST.get('category_name')
        try:
            if category_name:
                cn_regex = re.match(r'[а-яА-Яa-zA-Z0-9]*', category_name)
                if cn_regex.group(0):
                    existing = Category.objects.values().filter(name=category_name).exists()
                    if existing:
                        return render(request, 'square/AddCategory.html', context={'ERROR': 'Такой проект уже есть'})

                    Category.objects.create(name=category_name)
                return render(request, 'square/AddCategory.html')

        except TypeError as e:
            return render(request, 'square/AddCategory.html', context={'ERROR': 'Пустая категория'})


class AddProjectView(View):
    def get(self, request):
        exists_category = Category.objects.values()

        return render(request, 'square/AddProject.html', context={'exists_category': exists_category})

    def post(self, request):
        project_category = request.POST.get('project_category')
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        if project_category and project_name:
            pc = re.match(r'[а-яА-Яa-zA-Z0-9]*', project_category)
            pn = re.match(r'[а-яА-Яa-zA-Z0-9]*', project_name)
            if pc.group(0) and pn.group(0):
                Project.objects.create(name=pn.group(0), category_id=pc.group(0), description=description)
        return render(request, 'square/AddProject.html')
