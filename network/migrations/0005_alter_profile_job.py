# Generated by Django 4.2.1 on 2023-06-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_profile_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
