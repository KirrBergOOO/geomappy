from django.urls import path
from . import views
from django.conf.urls import url, include

#urlpatterns = [
#    path('', views.new, name='new'),
#    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

urlpatterns = [
    path('search', views.SearchResults, name='search'),
    path('', views.new, name='articles_list'),
    path('<slug:slug>', views.ArticlesDetailView.as_view(), name='articles_detail'),
    ]
#views.ArticlesListView.as_view()
