from django.urls import path
from . import views



urlpatterns = [
    path('', views.my_info, name='my_info'),
    path('/cart', views.cart, name='cart'),
    path('/heart', views.heart, name='heart'),

    # path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),

    # path('my_info/', include('my_info.urls')),
]
