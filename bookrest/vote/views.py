from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.utils.regex_helper import Choice
from .models import *
from .forms import *

# Create your views here.
def vote(request):
    #투표 중일때와 아닐 때 함수 만들어야함
    #투표 기능
    booklists = BookList.objects.all

    votes = BookList.objects.get(id = id)
    selection = request.POST['votes']
    votes.votes += 1
    votes.save()

    return redirect('vote')

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