from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, History
from .utils import decode_article
from .algorithm import get_recommendation_list

import time
import numpy as np


# Create your views here.

def index(request):
    random_ids = set(np.random.randint(1, 41, size=10))
    article_list = []
    for id in random_ids:
        article_list.append(decode_article(Article.objects.get(pk=id), True))
    context = {'article_list': article_list, 'recommendation_list': get_recommendation_list()}
    return render(request, 'view/index.html', context)


def article(request, article_id):
    h = History(article_id=article_id, date=int(time.time()))
    h.save()
    article = decode_article(get_object_or_404(Article, pk=article_id))
    context = {'article': article, 'recommendation_list': get_recommendation_list()}
    return render(request, 'view/article.html', context)


def thumb(request, article_id):
    # h = History(article_id=article_id, date=int(time.time()))
    # h.save()
    return HttpResponse('ok')
