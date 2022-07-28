from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
# Create your views here.
def new(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'news/articles_list.html', {'news': news})
class ArticlesListView(ListView):
    model = Articles
    template_name = 'news/articles_list.html'
class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'news/articles_detail.html'
class SearchResults(ListView):
    model = Articles
    template_name = 'news/search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Articles.objects.filter(title__icontains=query)
            return queryset
