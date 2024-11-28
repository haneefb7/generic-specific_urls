from django.urls import path
from tollywood.views import *

urlpatterns=[
    path('movies/',movies,name='movies')
]