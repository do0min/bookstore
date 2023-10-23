"""book_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import book.views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import MyInfoView

# path('', book.views.home, name = 'home'),
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('book.urls')),
    path('admin_panel', include("admin_panel.urls")),
    path('buy', include("buy_book.urls")),
    path('add', include('add_book.urls')),
    path('used', include('used_book.urls')),
    path('cart', views.cart_view, name='cart'),
    path('my_info/', MyInfoView.as_view() , name='my_info'),
    path('heart', views.heart_view, name='heart'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
