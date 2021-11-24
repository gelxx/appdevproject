from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length = 100, primary_key = True)
    content = models.CharField(max_length = 1000)
    date = models.DateField()