from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import *
from .forms import *

# Create your views here.
def vote(request):
    return render(request, 'vote.html')

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