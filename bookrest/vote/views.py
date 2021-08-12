from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.utils.regex_helper import Choice
from .models import *
from .forms import *
from join.models import *

# Create your views here.
def vote(request):
    booklists = BookList.objects
    return render(request, 'vote.html')

def getvote(request, pk):
    if not request.user.is_active:
        return HttpResponse('로그인을 해주세요')

    booklist = get_object_or_404(BookList, pk = pk)
    vote =  get_object_or_404(Vote, pk = pk)
    user = request.user

    if booklist.votes.filter(id = user.id).exists():
        return HttpResponse('이미 투표를 했습니다')
    else:
        booklist.votes += 1
        booklist.save()
    
    return redirect('getvote')
    

def addvote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.vote_date = timezone.now()
            vote.save()
            return redirect('vote')
    else:
        form = VoteForm()
        return render(request, 'vote/addvote.html', {'form':form})

def voteresult(request):
    return render(request, 'vote/voteresult.html')