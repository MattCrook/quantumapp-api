# Generated by Django 3.0.7 on 2021-01-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantumforum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuscode',
            name='description',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]