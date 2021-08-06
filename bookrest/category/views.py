from django.shortcuts import render
from .models import BookClassInfo

# Create your views here.
def category(request):
    categorys = BookClassInfo.objects.all()
    return render(request, 'category.html', {'categorys':categorys})
