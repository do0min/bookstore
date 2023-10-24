from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> f4ebe818224e47658765983b8c390f51ae5e55a2

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image')
    publisher = models.CharField(max_length=500)
    auther = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    sub_department = models.ForeignKey('SubDepartment', on_delete=models.CASCADE, null=True, default=None)

class Department(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
class SubDepartment(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='sub_departments')

    def __str__(self):
        return self.name
<<<<<<< HEAD

class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class BookCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_carts')
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

=======
>>>>>>> f4ebe818224e47658765983b8c390f51ae5e55a2
