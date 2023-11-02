from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy, name='buy'),
    path('/detail/<int:book_id>/', views.detail, name='detail'),
] 
