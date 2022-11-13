from django.db import models

# Create your models here.
class blogs(models.Model):
    title= models.CharField(max_length=20)
    content = models.TextField()

# class punya properti , ditransform di django jadi table dan column
# langkah pertama

class matematika(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()