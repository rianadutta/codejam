from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

# note -- ultimately what this program needs to do is to create a database entry
# of the course that it scraped

# program urls
math_comp_hon = "https://www.mcgill.ca/mathstat/undergraduate/programs/b-sc/joint-honours-mathematics-and-computer-science-b-sc"
math_comp = "https://www.mcgill.ca/study/2022-2023/faculties/science/undergraduate/programs/bachelor-science-bsc-major-computer-science"

def generate_url(course):
    endpoint = course.lower()
    endpoint = endpoint.replace(" ", "-")
    endpoint = "https://www.mcgill.ca/study/2022-2023/courses/" + endpoint
    return endpoint


def webscrape(course):
    url = generate_url(course)

    listofprereqs = []
    listofcoreqs = []
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    pattern = '<li><p>Prerequisite.*?/p>'
    match_results = re.search(pattern, html)
    if match_results is not None:
        title = match_results.group()
        
        pattern1 = "courses/.*?/a>"
        prereqs = re.findall(pattern1, title)
        for i in prereqs:
            i = i.split('>')[1] 
            i = i.split('<')[0]
            listofprereqs.append(i)
        print("Prereqs: " )
        print(listofprereqs)
    pattern2 = '<li><p>Corequisit.*?/p>'
    match_results1 = re.search(pattern2,html)
    if match_results1 is not None:
        title = match_results1.group()
        pattern1 = "courses/.*?/a>"
        coreqs = re.findall(pattern1, title)
        for i in coreqs:
            i = i.split('>')[1] 
            i = i.split('<')[0]
            listofcoreqs.append(i)
        print("Coreqs: " )
        print(listofcoreqs)
    return listofprereqs #, listofcoreqs

def webscrape1(course):
    url = generate_url(course)

<<<<<<< HEAD
    listofprereqs = []
    listofcoreqs = []
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    pattern = '<li><p>Prerequisite.*?/p>'
    match_results = re.search(pattern, html)
    if match_results is not None:
        title = match_results.group()
        length = len(title)
        title = title.split(',')
        if length == len(title[0]):
            title = title[0].split("and")
        for j in range(len(title)):
            list = []
            pattern1 = "courses/.*?/a>"
            prereqs = re.findall(pattern1, title[j])
            for i in prereqs:
                print(i)
                i = i.split('>')[1] 
                i = i.split('<')[0]
                print(i)
                list.append(i)
            listofprereqs.append(list)
        print("Prereqs: " )
        print(listofprereqs)
    pattern2 = '<li><p>Corequisit.*?/p>'
    match_results1 = re.search(pattern2,html)
    if match_results1 is not None:
        title = match_results1.group()
        pattern1 = "courses/.*?/a>"
        coreqs = re.findall(pattern1, title)
        for i in coreqs:
            i = i.split('>')[1] 
            i = i.split('<')[0]
            listofcoreqs.append(i)
        print("Coreqs: " )
        print(listofcoreqs)
    return listofprereqs, listofcoreqs

webscrape1("comp 252")

=======
>>>>>>> 75ac7e486322917c5d2910a04e6d3efb704764a7
def programscrape(program):
    page = urlopen(program)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    pattern = '>Required Courses'
    match_results = re.search(pattern, html)
    if match_results is not None:
        title = match_results.group()
    print(title)

#programscrape(math_comp)

def prog(program):
    page = requests.get(program)
    #print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find_all('div', id="block-system-main")
    pattern = re.compile("Required Courses")
    #print(div[0])
    #title = div[0].find(text=pattern)
    title = div[0].find(text="Required Courses").parent
    a = title.nextSibling
    for i in range(5):
        print(type(a))
        a = a.nextSibling
        
    b = a.parent.find('li')
    #print(a.nextSibling)
    #print(b.prettify())

#prog(math_comp_hon)
