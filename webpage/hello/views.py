import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .form import UserForm

def hello(request):
    #submitted = False
    program = "program"
    semester = " "
    courses = " "
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            program = form.data['program']
            semester = form.data['semester']
            courses = form.data['courses']
    else:
        form = UserForm()
        #if 'submitted' in request.GET:
            #submitted = True
    return render(request, "hello/hello.html", {"form": form, "program": program, "semester": semester, "courses": courses})


