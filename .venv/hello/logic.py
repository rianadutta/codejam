# getting the request

request = [Program, [taken Course], Fall/Winter, semesters, [elec Courses] ]

# search from program within sql database (program table)
program [[required] ,{complementary: int, list}]

listrequiredleft = for course in program.required: if course not in taken Course, add to listrequiredleft
dict complemntaryleft = dict program.complementary
for pair in complementaryleft:
    if complementaryleft[pair] in taken courses, complemtaryleft = complementaryleft -1

#check what required courses they are able to take
listofsemesters = []
avecoursesppersem = round(ints + len(required)) / sems
while (listrequiredleft):
    currentsem = []
    for i in required:
        # if i meets requirements
        i.append(currentsem)
        if currentsem > avecoursepersem: break
    

#filling in complementaries


