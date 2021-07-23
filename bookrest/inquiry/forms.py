from django import forms
from django.db.models import fields
from .models import *

class QInquiryForm(forms.ModelForm):
    class Meta:
        model = QInquiry
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'qtype', 'title', 'body']

class Answer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']