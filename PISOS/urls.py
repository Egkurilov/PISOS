"""PISOS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path


from Admin.views import LoginView, DashboardView, TaskTypeAddView, TaskAddView
from Calendar.views import CalendarView, AddCalendarView
from Square.views import SquareView, AddCategoryView, AddProjectView
from Board.views import BoardView

urlpatterns = [
        path('', SquareView.as_view()),
        path('category/add', AddCategoryView.as_view()),
        path('project/add', AddProjectView.as_view()),



        path('admin/login', LoginView.as_view()),
        path('admin/dashboard', DashboardView.as_view()),
        path('admin/task/type/add', TaskTypeAddView.as_view()),
        path('admin/task/add', TaskAddView.as_view()),

        path('calendar/', CalendarView.as_view()),
        path('calendar/add', AddCalendarView.as_view()),

        path('board/<int:pk>/', BoardView.as_view()),
]
