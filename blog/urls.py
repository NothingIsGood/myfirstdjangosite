from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^category/(?P<pk>\d+)$', views.category, name='category'), 
    url(r'^tag/(?P<pk>\d+)/$',views.tag, name='tag'),
    url(r'^page/(?P<pk>[0-9]+)/$', views.page_detail, name='page_detail'),
]