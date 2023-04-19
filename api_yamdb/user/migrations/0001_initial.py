# Generated by Django 3.2 on 2023-04-19 16:01

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(help_text='Имя пользователя', max_length=150, unique=True, validators=[user.validators.username_validator, user.validators.pattern_validator], verbose_name='Пользователь')),
                ('email', models.EmailField(help_text='Введите электронную почту', max_length=254, unique=True, verbose_name='Эл. почта')),
                ('bio', models.TextField(blank=True, help_text='Напишите пару фактов из биографии', verbose_name='Биография')),
                ('first_name', models.CharField(blank=True, help_text='Введите имя', max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Введите фамилию', max_length=150, verbose_name='Фамилия')),
                ('role', models.CharField(blank=True, choices=[('admin', 'Администратор'), ('moderator', 'Модератор'), ('user', 'Пользователь')], default='user', help_text='Выберите роль', max_length=150, verbose_name='Роль')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
