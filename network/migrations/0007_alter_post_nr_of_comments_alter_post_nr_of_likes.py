# Generated by Django 4.2.1 on 2023-06-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nr_of_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='nr_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
