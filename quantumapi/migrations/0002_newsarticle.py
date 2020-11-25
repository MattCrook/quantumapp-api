# Generated by Django 3.0.7 on 2020-11-23 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantumapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.utcnow, null=True)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('type', models.CharField(blank=True, max_length=60, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('article', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'newsarticle',
                'verbose_name_plural': 'newsarticles',
            },
        ),
    ]
