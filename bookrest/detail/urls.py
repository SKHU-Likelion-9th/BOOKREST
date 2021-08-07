from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("<str:id>/", views.detail, name="detail"),
    path("<str:id>/", views.wish, name="wish"),
] 