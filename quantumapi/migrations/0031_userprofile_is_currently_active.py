# Generated by Django 3.0.7 on 2021-01-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0030_auto_20210118_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_currently_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
