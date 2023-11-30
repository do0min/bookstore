from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsedBookCategoryForm, UsedBookForm, SearchForm
from .models import UsedBook  # 모델 임포트 필요
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    category_form = UsedBookCategoryForm(request.POST or None)
    used_books = UsedBook.objects.all()

    if category_form.is_valid():
        category = category_form.cleaned_data['category']
        if category:
            used_books = used_books.filter(category=category)

    items_per_page = 9
    paginator = Paginator(used_books, items_per_page)  # Change variable name to `used_books`

    page = request.GET.get('page')
    try:
        used_books = paginator.page(page)  # Change variable name to `used_books`
    except PageNotAnInteger:
        used_books = paginator.page(1)
    except EmptyPage:
        used_books = paginator.page(paginator.num_pages)

    context = {
        'used_books': used_books,
        'category_form': category_form,
    }
    return render(request, 'used_home.html', context)

@login_required
def used_up(request):
    if request.method == 'POST':
        form = UsedBookForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the user_id for the new UsedBook instance
            form.instance.user_id = request.user.id
            form.save()
            return redirect('add_used_book_success')
    else:
        form = UsedBookForm()

    return render(request, 'used_up.html', {'form': form})
    
    return render(request, 'used_up.html', {'form': form})

def add_used_book_success(request):
    return render(request, 'used_home.html')


def used_detail(request, used_id):
    used_book = get_object_or_404(UsedBook, pk=used_id)
    return render(request, 'used_detail.html', {'used_book': used_book})


def edit_book(request, used_id):
    used_book = get_object_or_404(UsedBook, pk=used_id)

    if request.method == 'POST':
        form = UsedBookForm(request.POST, request.FILES, instance=used_book)
        if form.is_valid():
            form.save()
            # Redirect or add additional logic as needed
    else:
        form = UsedBookForm(instance=used_book)

    return render(request, 'used_up.html', {'form': form, 'used_book': used_book})

def delete_book(request, used_id):
    used_book = get_object_or_404(UsedBook, pk=used_id)
    
    if request.method == 'POST':
        used_book.delete()
        return redirect('used')  # Redirect to the desired page after deletion

    return render(request, 'used_home.html', {'used_book': used_book})

@login_required  # 사용자 로그인이 필요한 경우
def add_heart(request, book_id):
    book = get_object_or_404(UsedBook, id=book_id)
    user_hearts = request.user.profile.hearts.all()
    context = {
        "book": book,
        "user_hearts": user_hearts,
    }
    if request.is_ajax():
        return JsonResponse({"message": "책을 관심 목록에 추가했습니다."})
    else:
        # 사용자가 브라우저에서 요청을 보낸 경우, 다른 앱의 템플릿을 렌더링하고 context 변수를 전달
        return render(request, 'heart.html', context)

@login_required
def add_cart(request, book_id):
    book = get_object_or_404(UsedBook, id=book_id)
    # 여기에서 장바구니에 책을 추가하는 로직을 구현
    return JsonResponse({"message": "책을 장바구니에 추가했습니다."})


def u_books(request, category):
    u_books = UsedBook.objects.filter(category=category)

    return render(request, 'used_home.html', {'u_books': u_books, 'category': category})