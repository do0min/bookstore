# forms.py
from django import forms
from .models import UsedBook 


class UsedBookForm(forms.ModelForm):
    class Meta:
        model = UsedBook
        fields = ['title', 'author', 'description', 'price', 'image', 'category']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='검색어')

class UsedBookCategoryForm(forms.ModelForm):
    class Meta:
        model = UsedBook
        fields = ['category']