from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.views import View
from django.db.models import Q
<<<<<<< HEAD
from .models import Cart
from django.shortcuts import get_object_or_404
=======
>>>>>>> f4ebe818224e47658765983b8c390f51ae5e55a2

def home(request):
    book = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Book.objects.filter(Q(name__icontains=search))
        context = {
            'result':results
        }
        return render(request, 'home.html', context)

        
    context = {
        'book':book,
    }
    return render(request, 'home.html', context)


def login(request):
    if request.method=="POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')   
        else:
            return render(request, 'login.html',{'error':'Username or password is incorrect!'}) 
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'signup.html',{'error':"Username is already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')

    return render(request,'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
<<<<<<< HEAD

def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart, created = Cart.objects.get_or_create(book=book)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('cart')  # 장바구니 페이지로 리다이렉트

def cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    # 장바구니에 이미 해당 상품이 있는지 확인
    cart_item, created = BookCart.objects.get_or_create(
        user=request.user,
        book=book,
    )

    # 이미 있는 경우 수량 증가, 없는 경우 새로 생성
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # 'cart'는 장바구니 페이지의 URL 이름으로 바꿔주세요
=======
>>>>>>> f4ebe818224e47658765983b8c390f51ae5e55a2
