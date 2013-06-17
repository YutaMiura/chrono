from django.http import HttpResponse
from django.template import Context, loader

from models import HolidayType, ArpHoliday

def view_arp_calendar(request):
    today = date.today()
    template = loader.get_template('arp_calendar/view_arp_calendar.html')
    
