from django.urls import path
from . import views

urlpatterns = [
    path('', views.used, name='used'),
    path('/used_up', views.used_up, name='used_up'),
    path('', views.add_used_book_success, name='add_used_book_success'),
    path('/used_detail/<int:used_id>/', views.used_detail, name='used_detail'),
    path('/search/', views.search, name='search'),
    path('add_heart/<int:book_id>/', views.add_heart, name='add_heart'),
    path('add_cart/<int:book_id>/', views.add_cart, name='add_cart'),
]