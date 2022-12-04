from datetime import datetime
from django.db import models

# Create your models here.
class Excursion(models.Model):
    MAX_VISITORS = int(15)
    TIMELINES = (
        '11:00 - 12:00', # СБ, ВС 
        '12:00 - 13:00', # ВС 
        '13:00 - 14:00', # СБ, ВС 
        '14:00 - 15:00', # СБ 
        '16:00 - 17:00', # СБ 
        '17:00 - 18:00', # СБ 
        '10:00 - 18:00', # СБ, ВС только для Без экскурсии
    )
    WEEKDAYS = (
        'Суббота', 'Воскресенье', 'Без экскурсии'
    )

    TIMELINES = tuple(zip(TIMELINES, TIMELINES))
    WEEKDAYS = tuple(zip(WEEKDAYS, WEEKDAYS))
    timelines = models.CharField(default=TIMELINES[0][0], max_length=20, choices=TIMELINES)
    weekdays = models.CharField(default=WEEKDAYS[0][0], max_length=20, choices=WEEKDAYS)
    number_of_visitors = models.IntegerField(default=0)
    total_visitors = models.IntegerField(default=MAX_VISITORS)
    is_available = models.BooleanField(default=True)
    is_shown = models.BooleanField(default=True)
    # title = models.CharField(default='', auto_created=True, max_length=50)


    def __str__(self):
        return f'{self.weekdays} {self.timelines}'
    

    def save(self, *args, **kwargs):
        self.title = f'{self.weekdays} {self.timelines}'
        super(Excursion, self).save(*args, **kwargs)