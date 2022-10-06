# Generated by Django 3.0.2 on 2022-10-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=250)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_answered', models.BooleanField(default=False)),
            ],
        ),
    ]