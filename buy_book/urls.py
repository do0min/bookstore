from django.urls import path, include
from book.views import *
from book.models import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

app_name = "buy_book"

urlpatterns = [
    path('', views.buy, name='buy'),
    path('/detail/<int:book_id>/', views.detail, name='detail'),
    # path('pay', include("book_pay.urls")),
] 
