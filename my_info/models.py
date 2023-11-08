from django.db import models
from django.contrib.auth.models import User 
# from .models import UsedBook


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


# class Cart(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)


class BookCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_Store_carts')
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.book.name}"


# class Cart(models .Model) :
#     cart_id = models.CharField(max_Length=250, blank=True)
#     date_added = models.DateField(auto_now_add=True)
#     class Meta:
#         db_table = "Cart"
#         ordering = ['date added']
#     def _str (self):
#         return self.cart_id 
    
# class CartItem(models .Model):
#     product = models. ForeignKey (UsedBook, on_deLete=models.CASCADE)
#     cart = models. ForeignKey (Cart, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     active = models. BooleanField (default=True)
#     class Meta:
#         db_table = 'CartItem'
#         def sub_total(self):
#             return self.product.price * self.quantity
#     def _str (self):
#         return self.product