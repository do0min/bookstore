from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsedBookForm, SearchForm
from .models import UsedBook  # 모델 임포트 필요
from django.db.models import Q

def search(request):
    form = SearchForm(request.GET)
    used_books = UsedBook.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        if search_query:
            used_books = used_books.filter(
                Q(title__icontains=search_query) | Q(author__icontains=search_query)
            )

    return render(request, 'used_home.html', {'used_books': used_books, 'form': form})


def used(request):
    if request.method == 'POST':
        pass

    used_books = UsedBook.objects.all()  # 모든 중고 책 가져오기
    return render(request, 'used_home.html', {'used_books': used_books})

def used_up(request):
    if request.method == 'POST':
        form = UsedBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_used_book_success')
    else:
        form = UsedBookForm()
    
    return render(request, 'used_up.html', {'form': form})

def add_used_book_success(request):
    return render(request, 'used_home.html')


def used_detail(request, used_id):
    used_book = get_object_or_404(UsedBook, pk=used_id)
    return render(request, 'used_detail.html', {'used_book': used_book})


  