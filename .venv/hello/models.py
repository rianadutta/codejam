from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=10)
    #pre-reqs = 
    #co-reqs =
    #restrictions = 
