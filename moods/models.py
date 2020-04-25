from django.db import models
from django.db.models import fields


class Mood(models.Model):
    date = fields.DateField()
    title = fields.CharField(max_length=50)
    image = models.ImageField()
    description = fields.TextField()

    def __str__(self):
        return str(self.date)
