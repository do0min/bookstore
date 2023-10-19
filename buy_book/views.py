from django.shortcuts import render, redirect
from book.models import *

def buy(request):
    return render(request,'buy_base.html')

def buy_detail(request):
    return render(request, 'buy_base.html')