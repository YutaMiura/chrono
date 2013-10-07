from django.db import models


class HolidayType(models.Model):
    name_en = models.CharField(max_length=30)
    name_ja = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name_ja

class ArpHoliday(models.Model):
    date = models.DateField(
        auto_now=False, auto_now_add=False, primary_key=True)
    holiday_type = models.ForeignKey('HolidayType')
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s:%s:%s" % (
            self.date.strftime('%Y/%m/%d'),self.name,self.holiday_type.name_ja)
    
