# Generated by Django 4.2.1 on 2023-06-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]