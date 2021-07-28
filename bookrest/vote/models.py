from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

#vote model
class Vote(models.Model):
    #투표설정
    vote_title = models.CharField(max_length=100)
    vote_date = models.DateField('date published')
    vote_explain = models.TextField()

    def __str__(self):
        return self.vote_title

#booklist model
class BookList(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='booklist')

    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)

    #순위, 투표수 설정
    rank = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.book_name