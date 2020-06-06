from django import forms
from .models import *

class ImagePostForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['image_caption', 'image_name', 'image']

class CommentsForm(forms.ModelForm):
  class Meta:
    model = Comments
    fields  = ['comments']