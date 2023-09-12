from django.db import models

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image')
    publisher = models.CharField(max_length=500)
    auther = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name