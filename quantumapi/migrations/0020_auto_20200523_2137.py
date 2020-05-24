# Generated by Django 3.0.6 on 2020-05-23 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quantumapi', '0019_auto_20200522_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='rollerCoaster_credits',
            new_name='rollerCoaster_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='owner_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BlacklistedToken',
        ),
    ]
