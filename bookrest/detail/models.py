from django.conf import settings
from django.db import models
from category.models import BookClassInfo

# Create your models here.

#찜하기 기능 구현을 위한 책 리스트와 user를 m2m으로 연결
class Wish(models.Model):
    book = models.ForeignKey(BookClassInfo, on_delete=models.CASCADE, related_name = 'wish')
    wishes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'wish')