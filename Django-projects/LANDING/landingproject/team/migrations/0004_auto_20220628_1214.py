# Generated by Django 2.2 on 2022-06-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20220628_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.CharField(blank=True, default='#', max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram',
            field=models.CharField(blank=True, default='#', max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.CharField(blank=True, default='#', max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.CharField(blank=True, default='#', max_length=50),
        ),
    ]
