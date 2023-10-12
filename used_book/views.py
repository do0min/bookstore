from django.shortcuts import render, redirect
from book.models import *

def used(request):
    return render(request,'used_base.html')