from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    date = models.CharField(max_length=100)
    comment_num = models.IntegerField(default=0)
    content = models.TextField()
    vector = models.TextField()


class History(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
