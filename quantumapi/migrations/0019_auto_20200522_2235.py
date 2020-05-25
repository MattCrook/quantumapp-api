# Generated by Django 3.0.6 on 2020-05-22 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quantumapi', '0018_delete_blacklistedtoken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'userProfile', 'verbose_name_plural': 'userProfiles'},
        ),
        migrations.CreateModel(
            name='BlacklistedToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(db_index=True, unique=True)),
                ('expires_at', models.DateTimeField(db_index=True)),
                ('blacklisted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]