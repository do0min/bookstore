from django.contrib import admin
from django.urls import path, include
from book.models import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('book.urls')),
    path('buy', include("buy_book.urls")),
    path('add', include('add_book.urls')),
    path('used', include('used_book.urls')),
    path('pay', include("book_pay.urls")),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

