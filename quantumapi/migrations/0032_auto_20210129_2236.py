# Generated by Django 3.0.7 on 2021-01-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0031_userprofile_is_currently_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_currently_active',
            field=models.CharField(blank=True, default='False', max_length=10, null=True),
        ),
    ]
