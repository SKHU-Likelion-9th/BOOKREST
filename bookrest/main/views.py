from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def introduce(request):
    return render(request, 'introduce.html')

def rule(request):
    return render(request, 'rule.html')