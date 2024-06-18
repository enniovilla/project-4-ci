from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class AccordionItem(models.Model):
    section = models.ForeignKey(Section, related_name='accordion_items', on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    body = models.TextField()

