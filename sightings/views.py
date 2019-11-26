from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('our app')
# Create your views here.
