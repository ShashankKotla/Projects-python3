from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField() #unlimit
    technology = models.CharField(max_length=40) #has limit
    image = models.FileField(upload_to="project_images/" , blank=True)
    
    
