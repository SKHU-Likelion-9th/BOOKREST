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

    major_인문 = BookClassInfo.objects.filter(department='인문융합자율학부')
    major_사회 = BookClassInfo.objects.filter(department='사회융합자율학부')
    major_미컨 = BookClassInfo.objects.filter(department='미디어콘텐츠융합자율학부')
    major_IT = BookClassInfo.objects.filter(department='IT융합자율학부')

    return render(request, 'category.html', {'book_list':book_list, 'search':search,' major_인문':major_인문,'major_사회':major_사회
        ,'major_미컨':major_미컨, 'major_IT':major_IT })