from django.urls import path
from . import views

app_name = "kakaopay"

urlpatterns = [
    path('', views.pay, name="pay"),
]