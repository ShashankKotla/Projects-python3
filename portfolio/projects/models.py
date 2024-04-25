from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=40)
    
