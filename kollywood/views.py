from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kollywood(request):
    return HttpResponse('some of the best movies of kollywood are VIKRAM, KHAIDI')