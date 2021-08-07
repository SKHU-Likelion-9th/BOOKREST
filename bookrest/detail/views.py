from django.http.response import HttpResponse
# from bookrest.category.models import BookClassInfo
# from bookrest.join.models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def detail(request):
    return render(request, 'detail.html')
#detail page
# def detail(request, id):
#     book = get_object_or_404(BookClassInfo, id = id)
#     return render(request, 'detail.html', {'book':book})

# #wish 기능
# def wish(request, id):
#     if not request.user.is_active:
#         return HttpResponse('로그인 해주세요')

#     book = get_object_or_404(BookClassInfo, id = id)
#     user = request.user

#     if book.wishes.filter(id = user.id).exists():
#         book.wishes.remove(user)
#     else:
#         book.wishes.add(user)
#     return redirect('detail', id)