from django.shortcuts import render, redirect,  get_object_or_404
from book.models import *
from django.shortcuts import render
from django.views import View

def buy(request):
    if request.method == 'POST':
        # 검색 폼을 제출했을 때의 처리 로직 추가
        pass

    # GET 요청일 경우, 모든 책 데이터를 가져옵니다.
    books = Book.objects.all()  # 모든 Book 모델 데이터를 가져옵니다.
    
    return render(request, 'main.html', {'result': books})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})


    