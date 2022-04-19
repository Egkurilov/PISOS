from django.shortcuts import render

# Create your views here.
from django.views import View
from ControlPanel.models import Category, Project
import re


class SquareView(View):
    def get(self, request):
        data_dict = {}

        projecties = Project.objects.values('id', 'description', 'name', 'category__name', 'category__id')

        for data in projecties:
            data_dict.setdefault(data['category__name'], {}).setdefault(data['category__id'], []).append(
                {'project_id': data['id'], 'project_name': data['name'], 'description': data['description']}
            )

        return render(request, 'square/Square.html', context={'projecties': data_dict})

