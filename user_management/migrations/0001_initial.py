# Generated by Django 4.2.7 on 2024-01-10 17:48

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import user_management.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(), django.core.validators.EmailValidator(message='Enter a valid email address.')])),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=6, message='Username must be at least 6 characters long.'), django.core.validators.MaxLengthValidator(limit_value=30, message='Username must not exceed 30 characters.')])),
                ('password', models.CharField(max_length=128, validators=[user_management.validators.validate_password_symbol, user_management.validators.validate_password_number, user_management.validators.validate_password_uppercase, user_management.validators.validate_password_lowercase, django.core.validators.MinLengthValidator(limit_value=6, message='Password must be at least 6 characters long.'), django.core.validators.MaxLengthValidator(limit_value=128, message='Password must not exceed 128 characters.')])),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('last_login_date', models.DateField(auto_now=True)),
                ('account_status', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='users', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]