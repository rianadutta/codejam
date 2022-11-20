import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_project.settings")

import django
django.setup()

# your imports, e.g. Django models
from hello.models import Program, Courses
from webscrape import webscrape

from treelib import Node, Tree
from tabulate import tabulate

def upper(thing):
    return thing.upper()

def course_list_parser(courses):
    list_courses = courses.split(",")
    print(list_courses)


def retrieve_course(course):
    try:
        c = Courses.objects.get(name=course)
    except Courses.DoesNotExist:
        p, co = webscrape(course)
        c = Courses(name=course, pre_reqs=p)
        #c = Courses(name=course, pre_reqs=p, co_reqs=co)
        c.save()
    return c

c = retrieve_course("COMP 250")
print(c.name)

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

def get_prereqs(list): # this is a placeholder function
    pre_req = []
    for i in range(len(list)):
        co = webscrape(list[i])
        pre_req.append(co)
    return pre_req

tree_list = []

def create_tree(tree_ptr, count, req, pre_req):
    for i in range(len(pre_req)):
        node = tree_list[count].get_node(tree_ptr)
        if node.data in pre_req[i]:
            tree_list[count].create_node(tag=req[i], identifier=req[i], data=req[i], parent=tree_ptr)

    l = tree_list[count].children(tree_ptr)
    for k in l:
        create_tree(k.identifier, count, req, pre_req)


def generate_output(program, courses_taken):
    global tree_list
    # p = Program.objects.filter(name=program)
    # req = p.required_courses # 1-d array
    # comp = p.complementary_courses # 2-d array

    req = ["MATH 222", "MATH 235", "MATH 242", "MATH 255"]
    req_left = []

    for i in req:
        if i not in courses_taken:
            req_left.append(i)

    # create_all_entries(courses_taken)
    # create_all_entries(req_left)

    pre_req = get_prereqs(req_left)

    for i in range(len(courses_taken)):
        tree_list.append(Tree())
        tree_list[i].create_node(tag=courses_taken[i], identifier=courses_taken[i], data=courses_taken[i])

    for i in range(len(tree_list)):
        create_tree(tree_list[i].root ,i, req_left, pre_req)
        tree_list[i].show()
    
    max_tree_depth = 0
    for j in tree_list:
        x = j.depth()
        if x > max_tree_depth:
            max_tree_depth = x

    table = []
    for i in range(max_tree_depth + 1):
        table.append([])
    
    for i in req:
        max_depth = 0
        for j in tree_list:
            if j.get_node(i) == None:
                x = 0
            else:
                x = j.depth(i)
            if x > max_depth:
                max_depth = x

        table[max_depth].append(i)
        print(max_depth)
    
    print(table)


# generate_output("a", ["MATH 141", "MATH 133"])