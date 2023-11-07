from django.shortcuts import render, redirect,  get_object_or_404
from book.models import *
from django.shortcuts import render
from django.views import View

def buy(request):
    if request.method == 'POST':
        pass

    books = Book.objects.all()  # 모든 Book 모델 데이터를 가져옵니다.
    
    return render(request, 'main.html', {'result': books})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})


    