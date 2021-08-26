from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Meme
from .forms import NewMemeForm
# Create your views here.
# memes = [
#     { "id": 1, "name": "Meme 1", "caption": "a meme caption" }, 
#     { "id": 2, "name": "Meme 2", "caption": "another meme caption"}
# ]
@login_required
def home(request):
    memes = Meme.objects.all()
    context = { "memes": memes }
    return render(request, 'memes/index.html', context)

def about(request):
    return render(request, 'memes/about.html')

@login_required
def create(request):
    if request.method == 'POST':
        item = NewMemeForm(request.POST)
        if item.is_valid():
            new_item = item.save()
            return redirect('show-meme', id=new_item.id)
    else:
        form = NewMemeForm()
        context = { "form": form }
        return render(request, 'memes/new.html', context)

@login_required
def show(request, id):
    meme = get_object_or_404(Meme, pk=id)
    context = { "meme": meme }
    return render(request, 'memes/show.html', context)
    
def not_found_404(request, exception):
    return render(request, {"message": "Page not found"})