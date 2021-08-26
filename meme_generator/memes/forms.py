from django import forms
from .models import Meme

class NewMemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['title', 'caption',  'image_url']