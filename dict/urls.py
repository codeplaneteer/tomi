from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home-page'),
    path('search/', search, name='search-page'),
]