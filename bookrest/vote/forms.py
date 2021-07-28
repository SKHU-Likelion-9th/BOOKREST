from django import forms
from django.db.models import fields
from .models import *

#투표 등록 폼
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['vote_title', 'vote_explain']

#투표 할 책 목록 작성 폼
class BookListForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = ['vote', 'book_name', 'book_author', 'book_publisher']