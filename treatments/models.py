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
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.header