from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("mushrooms, BREAD, and Minerva. They're all connected")
