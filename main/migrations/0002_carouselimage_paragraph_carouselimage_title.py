# Generated by Django 5.0.6 on 2024-06-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimage',
            name='paragraph',
            field=models.CharField(default='default paragaph', max_length=100),
        ),
        migrations.AddField(
            model_name='carouselimage',
            name='title',
            field=models.CharField(default='default title', max_length=30),
        ),
    ]