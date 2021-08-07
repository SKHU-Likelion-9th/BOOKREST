from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def noticeBase(request):
    return render(request, 'noticeBase.html')

def rule(request):
    return render(request, 'rule.html')