# coding: utf-8

from datetime import date
import calendar
from calendar import HTMLCalendar

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from models import HolidayType, ArpHoliday

class ARPHTMLCalendar(HTMLCalendar):
    '''
    ARPカレンダーをHTMLで表現するクラスです．
    '''

    def __init__(self, firstweekday):
        """
        constructor
        """
        super(HTMLCalendar, self).__init__(firstweekday)

    def formatmonth(self, year, month):
        """
        HTMLフォーマットのカレンダー情報を返します．カレンダー情報には
        指定年月の法定休日，法定外休日の情報が反映されます．
        """
        self.holidays = (
            ArpHoliday.objects.filter(date__year=int(year))
            .filter(date__month=int(month))
        )
        return super(ARPHTMLCalendar, self).formatmonth(year, month)

    def formatday(self, day, weekday):
        """
        一日分のテーブルデータ要素（td要素）を生成します．
        """
        if day != 0: # 0 means a day out of this month
            css_class = self.cssclasses[weekday]
            body = '<div class="daynumber">%d</div>' % day
        else:
            css_class = 'noday'
            body = '&nbsp;'
        return self.format_day_cell(css_class, body, day)

    def format_day_cell(self, css_class, body, the_day):
        """
        一日分のHTMLデータを生成します．休日であればその情報を反映した
        形式で返します．また土曜日は法定外休日(not statutory)，日曜日は
        法定休日(statutory)として扱います．

        the_dayは日付をですが，当月に含まれない日付の場合0(int)です．
        """

        holiday_content = ''
        idx_sun = len(self.cssclasses) - 1
        idx_sat = idx_sun - 1

        if css_class == self.cssclasses[idx_sun]:
            # statutory holiday
            holiday_content = self.get_holiday_content(1) 
        elif css_class == self.cssclasses[idx_sat]:
            # not statutory holiday
            holiday_content = self.get_holiday_content(2)

        for holiday in self.holidays:
            if holiday.date.day == the_day:
                holiday_content = (
                    self.get_holiday_content(
                        holiday.holiday_type_id,
                        holiday.name
                    )
                )
                
        day_cell_format = '''
        <td class="%s daycell" date="%d" halign="left" valign="top">
            %s
            <div class="daycontent">%s</div>
        </td>
        '''

        return (day_cell_format % 
                (css_class, the_day, body, holiday_content))

    def get_holiday_content(self, holiday_type, name=''):
        ht = HolidayType.objects.get(pk=holiday_type)
        content = '<div class="%s">%s</div>' % (ht.name_en, name)
        return content.encode('utf-8')

def list_calendar(request, year=None, month=None):
    """
    指定年月のカレンダーを表示します．
    """

    # Short cut version index view.
    # render() function takes following arguments:
    #  1. request object
    #  2. template name
    #  3. dictionaly represents the context
    # It returns an HttpRequest object 
    if year:
        year = int(year)
    else:
        year = date.today().year
    if month:
        month = int(month)
    else:
        month = date.today().month

    month_html = mark_safe(
        ARPHTMLCalendar(calendar.SUNDAY)
        .formatmonth(year, month))

    context = { 
        'year': year,
        'month': month,
        'month_html': month_html
    }
    return render(request, 'arp_calendar/list.html', context)
