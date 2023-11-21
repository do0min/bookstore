from django.urls import path, include
from book.views import *
from book.models import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *


urlpatterns = [
    path('', views.buy, name='buy'),
    path('/detail/<int:book_id>/', views.detail, name='detail'),
    path('/subdepartment/<str:subdepartment>/', books_sub, name='books_sub'),
    path('department/<str:department_name>/', department_books, name='department_books'),
    path('pick_up/<int:book_id>', views.pick_up, name='pick_up'),
    path('pick_up_buy/<int:book_id>', views.pick_up_buy, name='pick_up_buy'),
    # path('pay', include("book_pay.urls")),
] 
