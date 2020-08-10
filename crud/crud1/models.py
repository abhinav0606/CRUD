from django.db import models
import uuid,time,secrets

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=20,default="",primary_key=True)
    language=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name
