from django.shortcuts import render, redirect
from book.models import *
from django.shortcuts import render
from django.views import View

def buy(request):
    return render(request,'main.html')
def buy_detail(request):
    return render(request, 'detail.html')

