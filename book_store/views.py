

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