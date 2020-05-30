from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Mypage(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 50)
    Introduction = models.CharField(max_length = 50)
    
    body = models.TextField() 

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]   