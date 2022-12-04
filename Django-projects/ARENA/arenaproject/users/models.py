from excursions.models import Excursion
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# from arenaproject.settings import EMAIL_HOST_USER
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Userform(models.Model):
    EVENTS = (
        'Футбольный матч',
        'Хоккейный матч',
        'Концерт звезды',
        'Другое'
    )

    EVENTS = tuple(zip(EVENTS, EVENTS))
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=10, blank=False, unique=True)    
    email = models.EmailField()
    pd_argeement = models.BooleanField(default=True, verbose_name='Согласие на обработку персональных данных')
    email_send = models.BooleanField(default=False, verbose_name='Статус отправки email')
    email_status = models.BooleanField(default=False, verbose_name='Статус доставки email')
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, related_name='+')
    event = models.CharField(default=EVENTS[0][0], max_length=20, choices=EVENTS)

    # def increment_number_of_visitors(self, *args, **kwargs):
    #     self.excursion.number_of_visitors += 1
    #     # self.excursion.save()
    #     super(Excursion, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} // {self.excursion} // {self.staff.first_name} {self.staff.last_name}"
    

    def save(self, *args, **kwargs):
        # self.increment_number_of_visitors()
        self.excursion.number_of_visitors += 1
        super(Userform, self).save(*args, **kwargs)