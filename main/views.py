from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(600, cache='default', key_prefix='')
def main(request):
    return render(request, 'main/main.html')
