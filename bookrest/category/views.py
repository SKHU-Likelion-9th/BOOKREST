from django.core import paginator
from django.shortcuts import render
from .models import BookClassInfo
from django.core.paginator import Paginator

# Create your views here.
def category(request):
    book_sort = request.GET.get('sort', None)
    if book_sort == 'asc':
        books = BookClassInfo.objects.all().order_by('title') #책 제목 오름차순
    if book_sort == 'desc':
        books = BookClassInfo.objects.all().order_by('-title')#책 제목 내림차순 

    major_filter = request.GET.get('filter', None)
    if major_filter == 'major_인문':
        BookClassInfo.objects.filter(department='인문융합자율학부')
    if major_filter == 'major_사회':
        BookClassInfo.objects.filter(department='사회융합자율학부')
    if major_filter == 'major_미컨':
        BookClassInfo.objects.filter(department='미디어콘텐츠융합자율학부')
    if major_filter == 'major_IT':
        BookClassInfo.objects.filter(department='IT융합자율학부')
    #정렬 아직 적용 X, 프론트랑 합쳐야 됨 

    books = BookClassInfo.objects.all()
    paginator = Paginator(books, 4)
    page = request.GET.get('page') #몇번째 페이지인지 받아옴
    book_p = paginator.get_page(page) 

    return render(request, 'category.html', {'book_sort': book_sort, 'major_filter': major_filter, 'book_p':book_p })
