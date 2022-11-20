import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .form import UserForm

def hello(request):
    #submitted = False
    program = "program"
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #form.save()
            program = form.data['program']
            
            #HttpResponseRedirect('/form?submitted=True')
    else:
        form = UserForm()
        #if 'submitted' in request.GET:
            #submitted = True
    return render(request, "hello/hello.html", {"form": form, "program": program})


