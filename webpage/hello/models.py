from django.db import models
from django.contrib.postgres.fields import ArrayField

class Courses(models.Model):
    name = models.CharField(max_length=10)

    pre_reqs = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
            default=list,
        ),
        size=8,
        default=list,
    )

    co_reqs = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8,
        default=list,
    ),

    restrictions = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8,
        default=list,
    ),

    fall = models.BooleanField(default=False)
    winter = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)

    required_courses = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8,
        default=list,
    ),

    complementary_courses = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
            default=list,
        ),
        size=8,
        default=list,
    )

    def __str__(self):
        return self.name
