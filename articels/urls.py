
from django.conf.urls import url
from django.urls import path
from . import view
app_name = 'articles'
urlpatterns = [
    path('',view.article_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$',view.article_details , name='detail'),
]
