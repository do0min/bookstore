from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyInfoView.as_view(), name='my_info'),
    path('/cart', views.cart_view, name='cart'),
    path('/heart', views.heart_view, name='heart'),
]