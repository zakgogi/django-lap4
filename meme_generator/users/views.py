from django.shortcuts import redirect, render
from .forms import Signup


# Create your views here.
def signup(request):
    if request.method == 'POST':
        new_user = Signup(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('memes-home')
    else:
        form = Signup()
        context = { "form": form }
        return render(request, 'users/signup.html', context)