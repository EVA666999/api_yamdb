# Generated by Django 3.2 on 2023-04-13 11:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='ratingg',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
