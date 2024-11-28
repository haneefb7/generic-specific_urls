from django.urls import path
from bollywood.views import *

urlpatterns=[
    path('movies/',movies,name='movies')
]