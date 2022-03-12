from django.shortcuts import render
import calendar
from datetime import date

from django.views import View
import calendar as cd



class CalendarView(View):
    def get(self, request):
        loop_times = range(1, 13)
        month_name = []
        counter = 0
        dict_of_month = {}
        current_year = date.today().year
        for month in loop_times:
            month_name.append(cd.month_name[month])

        name_day_of_weak = cd.weekheader(3)
        for month in list(calendar.month_name)[1:]:
            counter += 1
            dict_of_month[month] = []
            dict_of_month[month].append(calendar.monthcalendar(current_year, counter))

        context = {
            'current_year': current_year,
            'month_name': month_name,
            'name_day_of_weak': name_day_of_weak,
            'calendar': calendar,
            'dict_of_month': dict_of_month,

        }

        return render(request, 'calendar/Calendartst.html', context)

    def post(self, request):
        pass


class AddCalendarView(View):
    def get(self, request):
        return render(request, 'calendar/Calendar.html')

    def post(self, request):
        pass
