from book.models import *
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.db.models import Q


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book,
    }
    return render(request, 'detail.html', context)


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
    subdepartment = SubDepartment.objects.get(name=subdepartment)
    books = subdepartment.booklist.all()

    items_per_page = 12
    paginator = Paginator(books, items_per_page)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'subdepartment': subdepartment,
        'books': books,
    }
    return render(request, 'books_sub.html', context)

def department_books(request, department_name):
    department = get_object_or_404(Department, name=department_name)
    subdepartments = SubDepartment.objects.filter(department=department)
    books = []
    for subdepartment in subdepartments:
        books.extend(subdepartment.booklist.all())

    context = {
        'department': department,
        'subdepartments': subdepartments,
        'books': books,
    }
    return render(request, 'books_sub_plus.html', context)

def pick_up(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'pick_up.html', {'book': book})

def pick_up_buy(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'pick_up_buy.html', {'book': book})
