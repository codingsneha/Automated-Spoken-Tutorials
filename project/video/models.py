#Creating a model here.

from django.db import models
class Topic(models.Model):
     """This is me creating the first model."""
text = models.CharField(max_length=200)
date_added = models.DateTimeField(
    auto_now_add=True)

def __str__(self):
    return self.text