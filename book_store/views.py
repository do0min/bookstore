from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.views import View
from django.db.models import Q


from django.shortcuts import render
from django.views import View
def base(self, request, *args, **kwargs):
        # 여기에 내 정보 페이지를 렌더링하는 로직을 추가할 수 있습니다.
        return render(request, 'base.html')
