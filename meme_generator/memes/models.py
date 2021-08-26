from django.db import models

# Create your models here.
class Meme(models.Model):
    title = models.CharField(max_length=80)
    image_url = models.CharField(max_length=300)
    caption = models.CharField(max_length=500)