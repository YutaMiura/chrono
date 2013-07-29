from datetime import date

from django.http import HttpResponse
from django.template import Context, loader

from models import HolidayType, ArpHoliday

def index(request):
    all_arp_holiday_list = ArpHoliday.objects.order_by('-date')
    template = loader.get_template('arp_calendar/index.html')
    context = Context({
            'all_arp_holiday_list': all_arp_holiday_list,
    })
    return HttpResponse(template.render(context))

# Short cut version index view.
# render() function takes following arguments:
#  1. request object
#  2. template name
#  3. dictionaly represents the context
# It returns an HttpRequest object 
#
# def index_by_shortcut(request):
#     from django.shortcuts import render
#     all_arp_holiday_list = ArpHoliday.objects.order_by('-date')[:3]
#     context = {'all_arp_holiday_list': all_arp_holiday_list}
#     return render(request, 'arp_calendar/index.html', context)

def list_calendar(request, year=None, month=None):
    if not year:
        year = date.today().year
    if not month:
        month = date.today().month

    holidaysInMonth = ArpHoliday.objects.filter(
        date__year=int(year), date__month=int(month))

    output = ', '.join([str(hd) for hd in holidaysInMonth])
    return HttpResponse(output)
