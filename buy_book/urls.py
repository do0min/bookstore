from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy, name='buy'),

    path('buy_detail/', views.buy_detail, name = 'buy_detail'),

    path('buy_detail/', views.buy_detail, name = 'buy_detail'),


] 