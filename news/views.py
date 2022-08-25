from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

# Create your views here.

def new(request):
    new = Articles.objects.order_by("-date")
    paginator = Paginator(new, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/articles_list.html', {'posts': posts, 'page': page})
class ArticlesListView(ListView):
    model = Articles
    template_name = 'news/articles_list.html'
class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'news/articles_detail.html'
def SearchResults(request):
    question = request.GET.get('q')
    if question:
        searched = Articles.objects.filter(title__icontains=question)
        template_name = 'news/search.html'
        return render(request, template_name, {'searched': searched, 'question': question})
    else:
        return render(request, 'news/search.html')
