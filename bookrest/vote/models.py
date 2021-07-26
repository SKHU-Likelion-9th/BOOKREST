from django.db import models

# Create your models here.

#vote model
class Vote(models.Model):
    #투표설정
    vote_title = models.CharField(max_length=100)
    vote_date = models.DateField('date published')
    vote_explain = models.TextField()
    
    #순위, 투표수 설정
    rank = models.IntegerField(default=0)
    vote = models.IntegerField(default=0)

#booklist model
class BookList(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name