# Generated by Django 4.2.5 on 2023-09-18 13:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10)])),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='meet_image')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('meetup', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='meetups.meetup')),
            ],
        ),
    ]