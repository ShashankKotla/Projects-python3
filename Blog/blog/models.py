from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30) #name of category set length max to 30

    class Meta:
        verbose_name_plural = "categories" #Here we provides correct plural form.
    def __str__(self): #__str__(), used to provide a better string representation of objects.
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #set's current time
    last_modified = models.DateTimeField(auto_now=True) #set's updated time
    categories = models.ManyToManyField("Category", related_name="posts") #sets relationship's

    def __str__(self): #__str__(), used to provide a better string representation of objects.
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post =  models.ForeignKey("post", on_delete = models.CASCADE) 
    #ForeignKey, set relation & tells django to delete all comments if the post id deleted.

    def __str__(self) -> str: # __str__(), used to provide a better string representation of objects.
        return f"{self.author} on '{self.post}'"


