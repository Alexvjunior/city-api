# Generated by Django 4.0.3 on 2022-04-06 23:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shell_opportunity', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('document_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MaxLengthValidator(11), django.core.validators.MinLengthValidator(11)])),
            ],
        ),
    ]
