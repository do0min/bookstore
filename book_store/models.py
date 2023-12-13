from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100) # 책 제목 정보
    author = models.CharField(max_length=100)  # 저자 정보 
    publisher = models.CharField(max_length=100)  # 출판사 정보 
    date = models.DateField()  # 출판일 정보 
    image = models.ImageField(upload_to='image') # 이미지 정보
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 가격 정보 
    stock = models.PositiveIntegerField()  # 재고 정보 
    delivery_info = models.CharField(max_length=100)  # 배송 정보 

    def __str__(self):
        return self.name