import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_project.settings")

import django
django.setup()

from hello.models import Program, Courses
from webscrape import webscrape

from treelib import Node, Tree

# initialize
mchR = ["COMP 206", "COMP 250", "COMP 252", "COMP 273", "COMP 302", "COMP 310", 
"COMP 330", "COMP 362", "MATH 222", "MATH 235", "MATH 251", "MATH 255", "MATH 350"]
mchP = ["COMP 202", "COMP 204", "COMP 208", "MATH 242", "MATH 254", "MATH 248", 
"MATH 358", "MATH 356", "MATH 357", "MATH 387", "MATH 454", "MATH 455", "MATH 456", "MATH 457"]

math_comp_hon = Program(name="Honours Math & Computer Science")
math_comp_hon.required_courses = mchR
math_comp_hon.complementary_courses = mchP
math_comp_hon.save()

def upper(thing):
    return thing.upper()

def main(program, courses):
    list_courses = course_list_parser(courses)


def course_list_parser(courses):
    list_courses = courses.split(",")
    return list_courses


def retrieve_course(course):
    try:
        c = Courses.objects.get(name=course)
    except Courses.DoesNotExist:
        pr, co, re = webscrape(course)
        c = Courses(name=course, pre_reqs=pr)
        c.pre_reqs = pr
        c.restrictions = re
        c.save()
    return c

# l = ["MATH 141"]
#c = retrieve_course(l[0])
#print(c.pre_reqs)

def get_prereqs(list): # this is a placeholder function
    pre_req = []
    for i in range(len(list)):
        co = webscrape(list[i])
        pre_req.append(co)
    return pre_req

tree_list = []

def create_tree(tree_ptr, count, req, pre_req, req_left):
    global tree_list

    for i in range(len(req_left)):
        val = pre_req[req_left[i]]
        node = tree_list[count].get_node(tree_ptr)

        for j in val:
            if node.data in j:
                tree_list[count].create_node(tag=req[i], identifier=req[i], data=req[i], parent=tree_ptr)

    l = tree_list[count].children(tree_ptr)
    for k in l:
        create_tree(k.identifier, count, req, pre_req, req_left)


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
    
    db_courses = []
    for i in range(len(req_left)):
        db_courses.append(retrieve_course(req_left[i]))
    
    pre_req = {}
    for i in db_courses:
        temp = []
        for j in i.pre_reqs:
            j = j.split(",")
            temp.append(j)

        pre_req[i.name] = temp
    
    co_req = {}
    for i in db_courses:
        co_req[i.name] = i.co_reqs
    
    restrictions = {}
    for i in db_courses:
        restrictions[i.name] = i.co_reqs


    # pre_req = get_prereqs(req_left)

    for i in range(len(courses_taken)):
        tree_list.append(Tree())
        tree_list[i].create_node(tag=courses_taken[i], identifier=courses_taken[i], data=courses_taken[i])

    for i in range(len(tree_list)):
        create_tree(tree_list[i].root, i, req_left, pre_req, req_left)
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

# generate_output("a", ["MATH 133", "MATH 141"])