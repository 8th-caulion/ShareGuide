from django.db import models
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    place = models.CharField(max_length = 20)
    tag = models.CharField(max_length = 100)
