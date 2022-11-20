from django.db import models
from django.contrib.postgres.fields import ArrayField

class Courses(models.Model):
    name = models.CharField(max_length=200)

    pre_reqs = ArrayField(
        models.CharField(max_length=200, blank=True),
        default=list,
    )

    co_reqs = ArrayField(
        models.CharField(max_length=200, blank=True),
        default=list,
    ),

    restrictions = ArrayField(
        models.CharField(max_length=200, blank=True),
        default=list,
    ),

    fall = models.BooleanField(default=False)
    winter = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)

    required_courses = ArrayField(
        models.CharField(max_length=200, blank=True),
        default=list,
    ),

    complementary_courses = ArrayField(
        models.CharField(max_length=200, blank=True),
        default=list,
    )

    def __str__(self):
        return self.name
