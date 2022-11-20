import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_project.settings")

import django
django.setup()

# your imports, e.g. Django models
from hello.models import Program, Courses


# from models import Program, Courses
from webscrape import webscrape

def upper(thing):
    return thing.upper()

def course_list_parser(courses):
    list_courses = courses.split(",")
    print(list_courses)


def retrieve_course(course):
    try:
        c = Courses.objects.get(name=course)
        return c
    except Courses.DoesNotExist:
        return -1

def validate(course, courses_taken):
    return False

def create_all_entries(list):
    """ Takes a list and web scrapes course entries for each list element
    if it did not already exist """
    for c in list:
        c2 = retrieve_course(c)
        if c2 == -1:
            webscrape(c)
            c2 = retrieve_course(c)
        c = c2
    return list

def generate_schedule(program, taken_courses, semesters):
    p = Program.objects.filter(name=program)
    req = p.required_courses # 1-d array
    comp = p.complementary_courses # 2-d array

    req_left = []
    complementariesleft = []

    # creates list of required courses that need to be taken
    for i in req:
        if i not in taken_courses:
            req_left.append(i)
    
    # creates 2-d array of complementary courses which need to be taken
    for section in comp:
        temp = []
        p = section[0]
        h = section[1:]
        for n in h:
            if n in taken_courses:
                p = p-1
            else:
                temp.append(n)
        if (p<0):
            p =0
        temp.insert(0, p)
        complementariesleft.append(temp)
    
    # do we need to do this for any other lists?
    create_all_entries(taken_courses)


    list_semesters = []
    for n in range(semesters):
        list_semesters[n] = []
    
    avecoursespersem = round(len(req) / semesters)

    while (req_left != []):
        for i in list_semesters:
            for j in req_left:
                if (validate(j) and len(list_semesters[i]) <= avecoursespersem):
                    list_semesters[i].append(j)
                    req_left.remove(j)
        

course_list_parser("COMP 202, MATH 310")