from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import Cart
from django.shortcuts import get_object_or_404
import logging

from django.shortcuts import render
from django.views import View

def cart_view(request, *args, **kwargs):
    # 여기에 장바구니 페이지를 렌더링하는 로직을 추가할 수 있습니다.
    return render(request, 'cart.html')

def heart_view(request, *args, **kwargs):
    # 여기에 장바구니 페이지를 렌더링하는 로직을 추가할 수 있습니다.
    return render(request, 'heart.html')


class MyInfoView(View):
    def get(self, request, *args, **kwargs):
        # 여기에 내 정보 페이지를 렌더링하는 로직을 추가할 수 있습니다.
        return render(request, 'my_info.html')




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

logger = logging.getLogger(__name__)


def delete_from_cart(request, book_id):
    # 해당 사용자의 장바구니에서 해당 책을 가져옴
    cart_item = get_object_or_404(BookCart, user=request.user, book__id=book_id)

    # 해당 장바구니 아이템 삭제
    cart_item.delete()

    logger.debug("Redirecting to cart page")
    return redirect('cart')