from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from instaapp.models import *

def register_view(request):
  if request.method == 'POST':  
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, 'You have successfully created your account!')
      return redirect('login')
  else:
    form = UserRegistrationForm()
  title = 'Register'
  return render(request, 'users/register.html', {'title':title, 'form':form})

@login_required
def profile(request):
  current_user = request.user
  user_images = Image.objects.filter(posted_by=current_user)
  return render(request, 'users/profile.html', {'user_images': user_images})