# Generated by Django 5.0.6 on 2024-06-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0005_alter_accordionitem_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accordionitem',
            name='duration',
            field=models.CharField(
                choices=[
                    ('30 minutes', '30 minutes'),
                    ('45 minutes', '45 minutes'),
                    ('60 minutes', '60 minutes')], max_length=50),
        ),
    ]
