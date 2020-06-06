from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
  image = models.ImageField(upload_to='images')
  image_name = models.CharField(max_length=40)
  image_caption = models.CharField(max_length=40)
  date_posted = models.DateTimeField(auto_now_add=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
  comments = models.TextField()
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(auto_now_add=True)