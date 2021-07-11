from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(request, 'mypage.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def sign_up(request):
    return render(request, 'sign_up.html')