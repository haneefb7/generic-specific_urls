from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def movies(request):
    return HttpResponse('Some of the best movies of tollywood are DEVARA, BAHUBALI, RRR')