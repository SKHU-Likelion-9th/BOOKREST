from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from .models import BookClassInfo
from join.models import CustomUser
from django.core.paginator import Paginator

# Create your views here.
# 검색과 페이징
def category(request):
    
    books = BookClassInfo.objects.all()
    search = request.GET.get('search', '')

    if search:
        books = books.filter(title__icontains=search)

    paginator = Paginator(books, 5)
    page = request.GET.get('page', '') #몇번째 페이지인지 받아옴
    book_list = paginator.get_page(page) #posts

    return render(request, 'category.html', {'book_list':book_list, 'search':search })
    
#detail 페이지 구현
#detail page
def detail(request, id):
    book = get_object_or_404(BookClassInfo, id = id)
    return render(request, 'detail.html', {'book':book})

#wish 기능
def wish(request, id):
    if not request.user.is_active:
        return HttpResponse('로그인 해주세요')
    
    book = get_object_or_404(BookClassInfo, id = id)
    user = request.user

    if book.wishes.filter(id = user.id).exists():
        book.wishes.remove(user)
        book.stock += 1
        book.save()

    else:
        book.wishes.add(user)
        book.stock -= 1
        book.save()
        
        if book.stock == 0:
            return HttpResponse('재고가 없습니다.')
    return redirect('detail', id = book.id)