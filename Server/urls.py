from django.urls import path

from . import views

urlpatterns = [
    path('<int:article_id>/', views.article, name='view'),
    path('thumb/<int:article_id>/', views.thumb, name='thumb'),
]
