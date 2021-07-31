from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm # 로그인, 회원가입 폼 
from .forms import UserCreationForm
# Create your views here.
def mypage(request): #마이페이지
    return render(request, 'mypage.html')

def sign_up(request): #회원가입
    context = {}
    if request.method == 'POST': #Post 방식 
        form = UserCreationForm(request.POST)
        if form.is_valid(): #유효성 검사 
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(email=email, password=raw_password)
            auth.login(request, user)
            return redirect('main')
        else:
            context['signup_form'] = form
            # return render(request, 'sign_up.html', {'form':form})
    else: #get 방식 
        form = UserCreationForm()
        context['signup_form'] = form
    return render(request, 'sign_up.html', context)

def sign_in(request): #로그인
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'sign_in.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'sign_in.html', {'form': form})

def sign_out(request): #로그아웃
    auth.logout(request)
    return redirect('main')
