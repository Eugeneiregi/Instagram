from django.urls import path, re_path, include
from . import views

urlpatterns=[
  path('home/', views.home, name='home'),
  path('post_image/', views.post_image, name='post_image'),
  path('single_image/<int:image_id>', views.single_image, name='single_image')
]