from django.db import models
# from django.contrib.auth.models import User
# from book.models import *


# class Cart(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     class Meta:
#         app_label = 'book_store'


# class BookCart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_Store_carts')
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.user.username} - {self.book.name}"
