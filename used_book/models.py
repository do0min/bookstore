from django.db import models
from django.contrib.auth.models import User
from django.db import models
class DetailImage(models.Model):
    image = models.ImageField(upload_to='books/images/')
    used_book = models.ForeignKey('UsedBook', on_delete=models.CASCADE, related_name='images') 

    def __str__(self):
        return f"Image {self.pk}"
class UsedBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/', null=True)
    # detail_image = models.ForeignKey(DetailImage, on_delete=models.CASCADE, related_name='used_books', null=True)
    detail_images = models.ManyToManyField(DetailImage)
    category = models.CharField(max_length=50, choices=[
        ('소프트웨어융합과', '소프트웨어융합과'),
        ('스마트IT과', '스마트IT과'),
        ('빅데이터과', '빅데이터과'),
        ('AI융합과', 'AI융합과'),
        ('패션디자인과', '패션디자인과'),
        ('세라믹디자인과', '세라믹디자인과'),
        ('니트패션디자인과', '니트패션디자인과'),
        ('산업디자인과', '산업디자인과'),
        ('문예창작과', '문예창작과'),
        ('인테리어디자인과', '인테리어디자인과'),
        ('식품영양과', '식품영양과'),
        ('스포츠건강관리과', '스포츠건강관리과'),
        ('유아교육과', '유아교육과'),
        ('보건행정과', '보건행정과'),
        ('호텔관광과', '호텔관광과'),
        ('실무영어과', '실무영어과'),
        ('서비스경영과', '서비스경영과'),
        ('비서인재과', '비서인재과'),
        ('실무일본어과', '실무일본어과'),
        ('실무중국어과', '실무중국어과'),
        ('외식산업과', '외식산업과'),
        ('세무회계과', '세무회계과'),
        ('행정실무과', '행정실무과'),
        ('항공과', '항공과'),
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    userid = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'{self.userid} - {self.date}'