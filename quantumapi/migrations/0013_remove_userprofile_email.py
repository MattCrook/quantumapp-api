# Generated by Django 3.0.6 on 2020-05-21 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0012_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
