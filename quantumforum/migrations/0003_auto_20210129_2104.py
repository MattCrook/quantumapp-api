# Generated by Django 3.0.7 on 2021-01-29 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quantumforum', '0002_statuscode_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendships',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
