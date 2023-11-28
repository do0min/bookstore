# forms.py
from django import forms
from .models import UsedBook 

class UsedBookForm(forms.ModelForm):
    class Meta:
        model = UsedBook
        fields = ['title', 'author', 'description', 'price', 'image', 'category']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='검색어')



class YourForm(forms.Form):
    # MultipleChoiceField를 사용하여 여러 파일 업로드
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))