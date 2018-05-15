# Created by Tei Michael on 2018/5/14.

from urllib import parse
import re


def decode_article(article, filter=False):
    article.title = parse.unquote(article.title)
    article.author = parse.unquote(article.author)
    article.content = parse.unquote(article.content)
    if filter:
        article.content = filter_tag_p(article.content)
    return article


def filter_tag_p(html_str):
    re_p = re.compile(r'<[^>]+>', re.S)
    return re_p.sub('', html_str)
