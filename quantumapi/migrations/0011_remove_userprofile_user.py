# Generated by Django 3.0.6 on 2020-05-21 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0010_auto_20200520_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
