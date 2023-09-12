from django.shortcuts import render, redirect
from book.models import *

def add(request):
    return render(request,'add_base.html')