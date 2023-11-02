from django.shortcuts import render, redirect
from book.models import *
from django.views import View

def my_info(request):
    return render(request,'my_info.html')

def cart(request):
    return render(request, 'cart.html')

def heart(request):
    return render(request, 'heart.html')


# from django.shortcuts import render
# from django.views import View
# from book.models import *


# class cart(View):
#     def get(self, request, *args, **kwargs):
#         # 장바구니 페이지 렌더링 및 필요한 로직 추가
#         return render(request, 'cart.html')

# class heart(View):
#     def get(self, request, *args, **kwargs):
#         # 관심 상품 페이지 렌더링 및 필요한 로직 추가
#         return render(request, 'heart.html')

# class my_info(View):
#     def get(self, request, *args, **kwargs):
#         # 내 정보 페이지 렌더링 및 필요한 로직 추가
#         return render(request, 'my_info.html')