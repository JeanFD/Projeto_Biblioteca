from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('livros/', LivrosView.as_view(), name='livros')
]