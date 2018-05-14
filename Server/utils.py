# Created by Tei Michael on 2018/5/14.

from urllib import parse


def decode_article(article):
    article.title = parse.unquote(article.title)
    article.author = parse.unquote(article.author)
    article.content = parse.unquote(article.content)
    return article
