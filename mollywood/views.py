from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mollywood(request):
    return HttpResponse('some of the best movies of mollywood are AVESHAM, LUCKY BHASKAR')