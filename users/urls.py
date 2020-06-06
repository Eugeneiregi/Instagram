from django.urls import path
from . import views

urlpatterns = [
  path('registration/', views.register_view, name = 'registration'),
  path('profile/', views.profile, name='profile')
]