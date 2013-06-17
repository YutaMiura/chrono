from django.db import models


class HolidayType(models.Model):
    name_en = models.CharField(max_length=30)
    name_ja = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name_ja

class ArpHoliday(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, primary_key=True)
    holiday_type = models.ForeignKey('HolidayType')

    def __unicode__(self):
        return self.date.strftime('%Y/%m/%d:') + self.holiday_type.name_ja
