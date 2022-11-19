import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .form import ProgramForm

def hello(request):
    form = ProgramForm(request.Post)
    return render(request, "hello/hello.html", {"form": form})


