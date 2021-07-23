from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *

# Create your views here.

#문의 목록 페이지
def inquiry(request):
    return render(request, 'inquiry.html')

#문의 글 작성 페이지
def ask(request):
    if request.method == 'POST':
        form = QInquiryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            form.save.m2m()
            return redirect('inquiry')
    else:
        form = QInquiryForm()
        return render(request, 'inquiry/ask.html', {'form' : form})
    
#작성 글 자세히 보기
def inqdetail(request):
    return render(request, 'inqdetail.html')

#관리자용 문의 답변 페이지
def answer(request):
    return render(request, 'answer.html')