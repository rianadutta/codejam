import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .form import UserForm
'''from tabulate import tabulate'''

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import logic



def hello(request):
    #submitted = False
    program = "program"
    semester = " "
    courses = " "
    col1 = ""
    col2 = ""
    col3 = ""
    col4 = ""
    col5 = ""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            program = form.data['program']
            semester = form.data['semester']
            courses = form.data['courses']

            table = logic.generate_output(program, courses)

            col1 = table[0]
            col2 = table[1]
            col3 = table[2]
            col4 = table[3]
            col5 = table[4]

    else:
        form = UserForm()
        #if 'submitted' in request.GET:
            #submitted = True
    return render(request, "hello/hello.html", {"form": form, "program": program, "semester": semester, "courses": courses, 
    "col1": col1, "col2": col2, "col3": col3, "col4": col4, "col5": col5})
