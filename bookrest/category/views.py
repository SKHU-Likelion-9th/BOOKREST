from django.shortcuts import render
from .models import BookClassInfo

# Create your views here.
def category(request):
    book_asc = BookClassInfo.objects.all().order_by('title') #책 제목 오름차순
    book_desc = BookClassInfo.objects.all().order_by('-title') #책 제목 내림차순 
    major_인문 = BookClassInfo.objects.filter(department='인문융합자율학부')
    major_사회 = BookClassInfo.objects.filter(department='사회융합자율학부')
    major_미컨 = BookClassInfo.objects.filter(department='미디어콘텐츠융합자율학부')
    major_IT = BookClassInfo.objects.filter(department='IT융합자율학부')

    return render(request, 'category.html', {
        'book_asc':book_asc,'book_desc':book_desc,'major_인문':major_인문,'major_사회':major_사회
        ,'major_미컨':major_미컨, 'major_IT':major_IT })
