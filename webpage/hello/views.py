import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, "hello/hello.html")