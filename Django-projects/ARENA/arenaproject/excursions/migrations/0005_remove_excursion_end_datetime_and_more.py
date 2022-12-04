# Generated by Django 4.1.2 on 2022-10-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0004_excursion_timelines_excursion_weekdays_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excursion',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='excursion',
            name='start_datetime',
        ),
        migrations.AlterField(
            model_name='excursion',
            name='timelines',
            field=models.CharField(choices=[('11:00 - 12:00', '11:00 - 12:00'), ('12:00 - 13:00', '12:00 - 13:00'), ('13:00 - 14:00', '13:00 - 14:00'), ('14:00 - 15:00', '14:00 - 15:00'), ('16:00 - 17:00', '16:00 - 17:00'), ('17:00 - 18:00', '17:00 - 18:00'), ('10:00 - 18:00', '10:00 - 18:00')], default='11:00 - 12:00', max_length=20),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='weekdays',
            field=models.CharField(choices=[('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье'), ('Без экскурсии', 'Без экскурсии')], default='Суббота', max_length=20),
        ),
    ]