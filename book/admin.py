from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('booklist',)

admin.site.register(Book)
