from django.conf.urls import url

from .views import article_list
from .views import article_create
from .views import article_detail

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)',article_list),
    url(r'^create/(?P<block_id>\d+)', article_create),
    url(r'^detail/(?P<aid>\d+)/$', article_detail),
]
