from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.inquiry, name="inquiry"), #문의하기
    path("ask", views.ask, name="ask"), #문의 글 작성 페이지
    path("inqdetail/", views.inqdetail, name="inqdetail"), #문의 글 자세히 보기 페이지
    path("answer", views.answer, name="answer"), #관리자용 문의 답변 페이지
] 