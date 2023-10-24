from django.shortcuts import render, get_object_or_404
from book.models import *

def books_sub(request, subdepartment): 
    # 문자열 값을 사용하여 SubDepartment 객체 검색
    subdepartment = SubDepartment.objects.get(name=subdepartment)
    books = subdepartment.booklist.all()

    context = {
        'subdepartment': subdepartment,
        'books': books,
    }
    return render(request, 'books_sub.html', context)


# def department_books(request, department_name):
#     department = get_object_or_404(Department, name=department_name)
#     subdepartments = SubDepartment.objects.filter(department=department)
#     books = subdepartments.first().booklist.all() if subdepartments.exists() else []

#     context = {
#         'department': department,
#         'books': books,
#     }

#     return render(request, 'books_sub_plus.html', context)

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
