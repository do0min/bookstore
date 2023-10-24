from django.urls import path
from . import views
<<<<<<< HEAD
from .views import add_to_cart
=======

>>>>>>> f4ebe818224e47658765983b8c390f51ae5e55a2
urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
<<<<<<< HEAD
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
=======
>>>>>>> f4ebe818224e47658765983b8c390f51ae5e55a2

]