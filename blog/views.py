from blog.models import Article
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "articles": Article.objects.filter(status='p').order_by('published')
    }
    return render(request, "blog/home.html", context)

