from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImagePostForm,CommentsForm
from django.contrib.auth.models import User
from .models import Image, Comments

@login_required
def home(request):
  images = Image.objects.all()
  return render(request, 'home.html', {'images': images})

@login_required
def post_image(request):
  current_user = request.user
  if request.method == 'POST':
    image_form = ImagePostForm(request.POST, request.FILES)
    if image_form.is_valid():
      image=image_form.save(commit=false)
      image.posted_by = current_user
      image.save()
      messages.success(request, 'Image saved successfully')
      return redirect('post_image')
  else:
    image_form = ImagePostForm()
  title='Post Image'
  return render(request, 'post_image.html', {"title":title, 'form':image_form})

@login_required
def single_image(request, image_id):
  current_user = request.user
  single_image = Image.objects.get(id = image_id)
  user_images = Image.objects.filter(posted_by=current_user)
  user_comments = Comments.objects.filter(posted_by=current_user)
  if request.method == 'POST':
    comments_form  = CommentsForm(request.POST)
    if comments_form.is_valid():
      comments = comments_form.save(commit=False)
      comments.posted_by = current_user
      comments.image = single_image
      comments.save()
      return redirect('single_image', image_id)
  else:
    comments_form = CommentsForm()
    title='single image'
  return render(request, 'single_image.html', {'title': title, 'comments_form': comments_form, 'single_image':single_image, 'user_images': user_images, 'user_comments':user_comments})