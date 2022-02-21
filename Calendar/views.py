from django.shortcuts import render

# Create your views here.
from django.views import View
import calendar as cd
c = cd.Calendar(firstweekday=1)

class CalendarView(View):
    def get(self, request):
        for i in c.yeardayscalendar(2022, 2):
            print(i)

        return render(request, 'calendar/Calendartst.html', context={'i': i})

    def post(self, request):
        pass


class AddCalendarView(View):
    def get(self, request):
        return render(request, 'calendar/Calendar.html')

    def post(self, request):
        pass
