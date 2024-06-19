from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class AccordionItem(models.Model):
    section = models.ForeignKey(Section, related_name='accordion_items', on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    body = models.TextField()

    DURATION_CHOICES = [
        ('30 minutes', '30 minutes'),
        ('45 minutes', '45 minutes'),
        ('60 minutes', '60 minutes'),
    ]

    duration = models.CharField(max_length=50, choices=DURATION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
