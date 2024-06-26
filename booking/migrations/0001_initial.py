# Generated by Django 5.0.6 on 2024-06-20 19:58

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('treatments', '0007_treatment_delete_accordionitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(
                    default=datetime.date.today)),
                ('time_arrival', models.TimeField(
                    default=datetime.time(12, 0))),
                ('time_leave', models.TimeField(
                    default=datetime.time(18, 0))),
                ('treatment', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='treatments.treatment')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
