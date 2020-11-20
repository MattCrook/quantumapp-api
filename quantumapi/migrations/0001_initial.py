# Generated by Django 3.0.7 on 2020-11-18 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.forms.widgets
import django.utils.timezone
import quantumapi.models.usermanager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='username')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=150, unique=True, verbose_name='password')),
                ('auth0_identifier', models.CharField(blank=True, max_length=50, null=True, verbose_name='auth0_identifier')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', quantumapi.models.usermanager.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'credit',
                'verbose_name_plural': 'credits',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name=django.forms.widgets.ClearableFileInput)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('origin_country', models.CharField(blank=True, max_length=50, null=True)),
                ('company_website', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'manufacturer',
                'verbose_name_plural': 'manufacturers',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parkLocation', models.CharField(max_length=50)),
                ('parkCountry', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'park',
                'verbose_name_plural': 'parks',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RollerCoaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_height', models.CharField(max_length=50)),
                ('max_speed', models.CharField(max_length=50)),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rollercoasters', to='quantumapi.Manufacturer')),
                ('park', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rollercoasters', to='quantumapi.Park')),
            ],
            options={
                'verbose_name': 'rollerCoaster',
                'verbose_name_plural': 'rollerCoasters',
                'ordering': ('manufacturer',),
            },
        ),
        migrations.CreateModel(
            name='Tracktype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'tracktype',
                'verbose_name_plural': 'tracktypes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quantumapi.Image')),
                ('rollerCoaster_id', models.ManyToManyField(through='quantumapi.Credit', to='quantumapi.RollerCoaster')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'userProfile',
                'verbose_name_plural': 'userProfiles',
            },
        ),
        migrations.AddField(
            model_name='rollercoaster',
            name='tracktype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rollercoasters', to='quantumapi.Tracktype'),
        ),
        migrations.AddField(
            model_name='rollercoaster',
            name='user_credit_id',
            field=models.ManyToManyField(through='quantumapi.Credit', to='quantumapi.UserProfile'),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('timestamp', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quantumapi.UserProfile')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'ordering': ('timestamp',),
            },
        ),
        migrations.AddField(
            model_name='credit',
            name='rollerCoaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='quantumapi.RollerCoaster'),
        ),
        migrations.AddField(
            model_name='credit',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='quantumapi.UserProfile'),
        ),
    ]
