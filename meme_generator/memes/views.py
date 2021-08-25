from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
memes = [
    { "id": 1, "name": "Meme 1", "caption": "a meme caption" }, 
    { "id": 2, "name": "Meme 2", "caption": "another meme caption"}
]

def home(request):
    context = { "memes": memes }
    return render(request, 'memes/index.html', context)

def about(request):
    return render(request, 'memes/about.html')

def show(request, id):
    meme = [meme for meme in memes if id == meme['id']][0]
    return HttpResponse(
        f"<p>Title: {meme['name']}, caption: {meme['caption']}</p>"
    )
