# Generated by Django 3.0.7 on 2020-11-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0003_auto_20201127_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='access_token',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
    ]
