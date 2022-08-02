from django.shortcuts import render
from .forms import IdeasForm
# Create your views here.
def ideas(request):

    if request.method == "POST":
        form = IdeasForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = IdeasForm()

    return render(request, 'ideas/ideas.html', {'form': form})
