# Generated by Django 3.0.7 on 2020-12-31 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0026_auto_20201229_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='cookies',
            field=models.TextField(blank=True, null=True),
        ),
    ]