from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.vote, name="vote"),
    path("getvote/<int:pk>/", views.vote, name="getvote"),
    path("voteresult/", views.voteresult, name="voteresult"), #투표 결과 페이지
    path("addvote/", views.addvote, name="addvote"), #어드민용 투표 등록 페이지
]