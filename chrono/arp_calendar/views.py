from datetime import date

from django.http import HttpResponse

from models import HolidayType, ArpHoliday

def index(request):
    return HttpResponse("hello world, this is Chrono Calendar view.")

def list_calendar(request, year=None, month=None):
    if not year:
        year = date.today().year
    if not month:
        month = date.today().month

    holidaysInMonth = ArpHoliday.objects.filter(
        date__year=int(year), date__month=int(month))

    output = ', '.join([str(hd) for hd in holidaysInMonth])
    return HttpResponse(output)
