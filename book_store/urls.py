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
from .views import *
from book.views import *
from book.models import *

from django.conf import settings
from django.conf.urls.static import static



# path('', book.views.home, name = 'home'),
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('book.urls')),
    path('admin_panel', include("admin_panel.urls")),
    path('buy', include("buy_book.urls")),
    path('add', include('add_book.urls')),
    path('used', include('used_book.urls')),

    # 학과별 책목록
    # path('subdepartment/<int:id>/',books_sub, name='books_sub'),
    # path('subdepartment/<subdepartment>/', books_sub, name='books_sub'),
    path('subdepartment/<str:subdepartment>/', books_sub, name='books_sub'),
    # path('department/<str:department>/', books_sub, name='books_sub'),
    path('department/<str:department_name>/', department_books, name='department_books'),


    # path('subdepartment/<int:subdepartment_id>/', books_sub, name='books_sub'),
    
    # path('future-ict/', books_sub, name='future_ict'),
    # path('software/', books_sub, name='software_convergence'),
    # path('smart-it/', books_sub, name='smart_it'),
    # path('big-data/', books_sub, name='big_data'),
    # path('ai/', books_sub, name='ai_convergence'),

    # path('fusion-design/', books_sub, name='fusion_design'),
    # path('fashion-design/', books_sub, name='fashion_design'),
    # path('ceramic-design/', books_sub, name='ceramic_design'),
    # path('knit-fashion-design/', books_sub, name='knit_fashion_design'),
    # path('industrial-design/', books_sub, name='industrial_design'),
    # path('literary-arts/', books_sub, name='literary_arts'),
    # path('interior-design/', books_sub, name='interior_design'),
    # path('human-service/', books_sub, name='human_service'),
    # path('food-nutrition/', books_sub, name='food_nutrition'),
    # path('sports-healthcare-management/', books_sub, name='sports_healthcare_management'),
    # path('early-childhood-education/', books_sub, name='early_childhood_education'),
    # path('health-administration/', books_sub, name='health_administration'),
    # path('global-service/', books_sub, name='global_service'),
    # path('hotel-tourism/', books_sub, name='hotel_tourism'),
    # path('practical-english/', books_sub, name='practical_english'),
    # path('service-management/', books_sub, name='service_management'),
    # path('secretarial-talent/', books_sub, name='secretarial_talent'),
    # path('practical-japanese/', books_sub, name='practical_japanese'),
    # path('practical-chinese/', books_sub, name='practical_chinese'),
    # path('catering-industry/', books_sub, name='catering_industry'),
    # path('tax-accounting/', books_sub, name='tax_accounting'),
    # path('administrative-practice/', books_sub, name='administrative_practice'),
    # path('aviation/', books_sub, name='aviation'),
    

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
