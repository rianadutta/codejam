import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .form import ProgramForm

def hello(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProgramForm()
    return render(request, "hello/hello.html", {"form": form})
    #return render(request, "hello/hello.html")


