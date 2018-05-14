from .models import Article
from .utils import decode_article


def get_recommendation_list():
    result = []
    for id in get_recommendation_ids():
        result.append(decode_article(Article.objects.get(pk=id)))
    return result


# Finish this function and return the list of recommendation ids
def get_recommendation_ids():
    result = [1]
    return result
