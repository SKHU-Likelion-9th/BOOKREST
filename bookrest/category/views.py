from django.core import paginator
from django.shortcuts import render
from .models import BookClassInfo
from django.core.paginator import Paginator
#from .filters import BookMajorFilter

# Create your views here.
# 검색과 페이징
def category(request):
    
    books = BookClassInfo.objects.all()
    search = request.GET.get('search', '')
    sort_val = books

    if search:
        books = books.filter(title__icontains=search)
        sort_val = books

    major = request.GET.get('major', '')
    if major == "인문":
        major_list = BookClassInfo.objects.filter(department='인문융합자율학부')
        sort_val = major_list
    if major == "사회":
        major_list = BookClassInfo.objects.filter(department='사회융합자율학부')
        sort_val = major_list
    if major == "미컨":
        major_list = BookClassInfo.objects.filter(department='미디어콘텐츠융합자율학부')
        sort_val = major_list
    if major == "IT":
        major_list = BookClassInfo.objects.filter(department='IT융합자율학부')
        sort_val = major_list

    paginator = Paginator(sort_val, 9)
    page = request.GET.get('page', '') #몇번째 페이지인지 받아옴
    book_list = paginator.get_page(page) #posts


    return render(request, 'category.html', {'book_list':book_list, 'search':search, 'major':major})
