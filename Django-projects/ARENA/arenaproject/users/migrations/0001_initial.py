# Generated by Django 4.1.2 on 2022-10-27 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('excursions', '0005_remove_excursion_end_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.TextField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('pd_argeement', models.BooleanField(default=True)),
                ('email_send', models.BooleanField(default=True)),
                ('email_status', models.BooleanField(default=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.CharField(choices=[('Футбольный матч', 'Футбольный матч'), ('Хоккейный матч', 'Хоккейный матч'), ('Концерт звезды', 'Концерт звезды'), ('Другое', 'Другое')], default='Футбольный матч', max_length=20)),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excursions.excursion')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]