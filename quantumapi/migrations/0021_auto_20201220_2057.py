# Generated by Django 3.0.7 on 2020-12-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0020_auto_20201220_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlog',
            name='environment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='headers',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='host_ip',
            field=models.TextField(blank=True, null=True),
        ),
    ]
