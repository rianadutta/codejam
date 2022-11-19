import requests
fomr .models import Program, Courses
# getting the request 
r = requests.get(url = URL, params = PARAMS)

#formatting info from the request
program = 'Computer Science'
coursestaken = ['COMP 202']
winterfall = True
semesters = 8
wanted = ['MATH 340', 'COMP 360']


# search from program within sql database (program table)
result = sqlsearch(program)
#(result has fields result.name, result.required, result.complementary)

requiredcoursesleft = []
for course in result.required:
    if course not in coursestaken:
        requiredcoursesleft.append(course)

complementariesleft = []

for section in complementariesleft:
    p = section[0]
    h = section[1:]
    for n in h:
        if n in coursestaken:
            p = p-1
        h.remove(n)
    if (p<0):
        p =0
    complementariesleft.append(p)
    for k in h:
        complementariesleft.append(k)

#given the name of a course (string), searches database and returns the Course class with
#all relevant attributes
def retrieve(course):
    out = sqlsearch database(course)
    if(out == -1):
        webscrape.py(course)
        out = sqlsearch database(course)
    return out

#these lists modify the original lists but instead of having a string of course name, it 
#has a Course (class) with all prereq etc attributes

infocoursestaken = []
inforequiredcoursesleft = []
infocomplementariesleft = []

def validate(course):
    #check if they can take course based on prereqs, coreqs, restrictions
    return True
def update(course, semester):
    #updates course lists assuming 
for course in coursestaken: 
    infocoursestaken.append(retrieve(course))

for course in requiredcoursesleft:
    inforequiredcoursesleft.append(retrieve(course))

for clump in complementariesleft:
    h = []
    infocomplementariesleft.append(clump[0])
    for course in clump[1:]:
        infocomplementariesleft.append(retrieve(course))

#check what required courses they are able to take
listofsemesters = {}


for n in range(semesters):
    listofsemesters[str(n)] = []
avecoursespersem = round(ints + len(required) / semesters)
while (requiredcoursesleft):
    for i in listofsemesters:
        for p in requiredcoursesleft:
            if(validate(p) and listofsemesters[i] <= avecoursespersem):
                listofsemesters[i].append(p)
                requiredcoursesleft.remove(p)

        

#filling in complementaries
#go through requests
for n in requests:
    if n meets requirements, add it to the first list in list of semesters that has room

return the list of semesters as a post request


