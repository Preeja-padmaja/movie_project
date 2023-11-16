from django.db import models

# Create your models here.
class movie_table(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.CharField(max_length=250)
    image=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.name


