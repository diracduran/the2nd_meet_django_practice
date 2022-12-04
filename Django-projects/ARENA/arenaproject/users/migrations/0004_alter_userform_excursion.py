# Generated by Django 4.1.2 on 2022-11-12 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0005_remove_excursion_end_datetime_and_more'),
        ('users', '0003_alter_userform_email_send_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='excursion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='excursions.excursion'),
        ),
    ]