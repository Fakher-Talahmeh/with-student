from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name