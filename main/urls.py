from django.contrib import admin
from django.urls import path

from .views import MainPageView, ArticleDetailView

app_name = 'main'

urlpatterns = [
    path('', MainPageView.as_view(), name='index_page'),
    path('article/<slug:article_slug>/', ArticleDetailView.as_view(), name='show_article'),

]
