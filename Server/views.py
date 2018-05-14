from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, History
from .utils import decode_article
from .algorithm import get_recommendation_list

import time


# Create your views here.

def index(request):
    article_list = Article.objects.all()[:5]
    for article in article_list:
        article = decode_article(article)
    context = {'article_list': article_list, 'recommendation_list': get_recommendation_list()}
    return render(request, 'view/index.html', context)


def article(request, article_id):
    print(article_id)
    h = History(article_id=article_id, date=int(time.time()))
    h.save()
    article = decode_article(get_object_or_404(Article, pk=article_id))
    context = {'article': article, 'recommendation_list': get_recommendation_list()}
    return render(request, 'view/article.html', context)


def thumb(request, article_id):
    # h = History(article_id=article_id, date=int(time.time()))
    # h.save()
    return HttpResponse('ok')
