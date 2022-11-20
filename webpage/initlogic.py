import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_project.settings")

import django
django.setup()

# your imports, e.g. Django models
from hello.models import Program, Courses
from webscrape import webscrape

from treelib import Node, Tree

mchR = ["COMP 206", "COMP 250", "COMP 252", "COMP 273", "COMP 302", "COMP 310", 
"COMP 330", "COMP 362", "MATH 222", "MATH 235", "MATH 251", "MATH 255", "MATH 350"]
mchP = ["COMP 202", "COMP 204", "COMP 208", "MATH 242", "MATH 254", "MATH 248", 
"MATH 358", "MATH 356", "MATH 357", "MATH 387", "MATH 454", "MATH 455", "MATH 456", "MATH 457"]


math_comp_hon = Program(name="Honous Math & Computer Science", required_courses=mchR, complementary_courses=mchP)