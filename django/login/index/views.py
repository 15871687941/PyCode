from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.


def main(request):
    articles = Article.objects.all()
    return render(request, 'index.html', context={'articles': articles})
