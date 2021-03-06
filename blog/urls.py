from django.urls import path
from .views import authors, category, home, detail

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('article/<slug:slug>/', detail, name="detail"),
    path('category/<slug:slug>/', category, name="category"),
    path('authors/', authors, name="authors"),
]

