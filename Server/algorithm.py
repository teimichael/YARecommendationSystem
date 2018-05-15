import numpy as np
import pandas as pd

from .models import Article, History
from .utils import decode_article


def get_recommendation_list():
    result = []
    for id in get_recommendation_ids():
        result.append(decode_article(Article.objects.get(pk=id)))
    return result


def cos_distance(vector_series, user_model):  # np.array
    sum_up = (vector_series * user_model).sum(axis=1)
    sqrt_a = np.sqrt((vector_series ** 2).sum(axis=1))
    sqrt_b = np.sqrt((user_model ** 2).sum())
    res = sum_up / (sqrt_a * sqrt_b)
    return res


def vector_normalize(vector_array):
    vector_len_list = np.sqrt((vector_array ** 2).sum(axis=1, keepdims=True))
    res = vector_array / vector_len_list
    return res


def calc_cos_dis_median(article_vectors_list):  # np.array
    # normalization
    # article_vectors_list = np.array(article_vectors_list.tolist())
    normal_vectors_list = vector_normalize(article_vectors_list)
    sqrt_sum = np.sqrt(((normal_vectors_list.sum(axis=0)) ** 2).sum())
    part_sum = normal_vectors_list.sum(axis=0)
    x1 = part_sum / sqrt_sum
    x2 = -x1
    distance_sum1 = (normal_vectors_list * x1).sum()
    distance_sum2 = (normal_vectors_list * x2).sum()
    if distance_sum1 > distance_sum2:
        res = x1
    else:
        res = x2
    return res


def str2float(article_vecs):
    res = []
    for vec in article_vecs:
        res.append([float(n) for n in vec[1:-1].split(',')])
    return res


# Finish this function and return the list of recommendation ids
def get_recommendation_ids():
    article_list = Article.objects.all()
    history_list = History.objects.all()
    article_ids = [obj.id for obj in article_list]
    article_vecs = [obj.vector for obj in article_list]
    article_vecs = str2float(article_vecs)
    article_frame = pd.DataFrame({'id': article_ids, 'vector': article_vecs}, columns=['id', 'vector'])
    history_ids = [obj.article_id for obj in history_list]
    user_viewed_frame = article_frame[article_frame['id'].isin(history_ids)]
    if user_viewed_frame.shape[0]==0:
        return article_ids[0:5]
    user_not_viewed_frame = article_frame[article_frame['id'].isin(history_ids) == False]
    user_model = calc_cos_dis_median(np.array(user_viewed_frame['vector'].values.tolist()))
    user_not_viewed_frame['distance'] = cos_distance(np.array(user_not_viewed_frame['vector'].values.tolist()),
                                                     user_model)
    user_not_viewed_frame = user_not_viewed_frame.sort_values(by='distance', ascending=False)

    # max to 5 by default
    result = user_not_viewed_frame['id'].values[0:5]
    return result