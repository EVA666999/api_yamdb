# Generated by Django 3.2 on 2023-04-16 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmation_code',
        ),
    ]
