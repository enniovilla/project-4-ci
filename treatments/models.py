from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Treatment(models.Model):
    section = models.ForeignKey(
        Section, related_name='treatment_items', on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    body = models.TextField()

    DURATION_CHOICES = [
        ('30 minutes', '30 minutes'),
        ('45 minutes', '45 minutes'),
        ('60 minutes', '60 minutes'),
    ]

    duration = models.CharField(max_length=50, choices=DURATION_CHOICES)

    def __str__(self):
        return f'{self.header}'
