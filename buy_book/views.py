from book.models import *
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.db.models import Q

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})


def buy(request):
    book = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Book.objects.filter(Q(name__icontains=search))
        context = {
            'result':results
        }
        return render(request, 'main.html', context)

        
    context = {
        'book':book,
    }
    return render(request, 'main.html', context)


def books_sub(request, subdepartment): 
    # 문자열 값을 사용하여 SubDepartment 객체 검색
    subdepartment = SubDepartment.objects.get(name=subdepartment)
    books = subdepartment.booklist.all()

    context = {
        'subdepartment': subdepartment,
        'books': books,
    }
    return render(request, 'books_sub.html', context)


def department_books(request, department_name):
    # Department 객체 가져오기
    department = get_object_or_404(Department, name=department_name)

    # Department에 속한 SubDepartment 가져오기
    subdepartments = SubDepartment.objects.filter(department=department)

    # 책 목록 가져오기
    books = []
    for subdepartment in subdepartments:
        books.extend(subdepartment.booklist.all())

    context = {
        'department': department,
        'books': books,
    }

    return render(request, 'books_sub_plus.html', context)


def pick_up(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'pick_up.html', {'book': book})

def pick_up_buy(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'pick_up_buy.html', {'book': book})