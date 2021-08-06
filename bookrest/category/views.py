
from django.core import paginator
from django.shortcuts import render
from .models import BookClassInfo
from django.core.paginator import Paginator

# Create your views here.
# 검색과 페이징
def category(request):
    
    books = BookClassInfo.objects.all()
    search = request.GET.get('search', '')

    if search:
        books = books.filter(title__icontains=search)

    paginator = Paginator(books, 9)
    page = request.GET.get('page', '') #몇번째 페이지인지 받아옴
    book_list = paginator.get_page(page) #posts

    return render(request, 'category.html', {'book_list':book_list, 'search':search })