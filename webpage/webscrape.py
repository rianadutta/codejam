from urllib.request import urlopen
# import requests
# from bs4 import BeautifulSoup
import re

# note -- ultimately what this program needs to do is to create a database entry
# of the course that it scraped

def generate_url(course):
    endpoint = course.lower()
    endpoint = endpoint.replace(" ", "-")
    endpoint = "https://www.mcgill.ca/study/2022-2023/courses/" + endpoint
    return endpoint


def webscrape(course):
    url = generate_url(course)

    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    pattern = '<li><p>Prerequisite.*?/p>'
    match_results = re.search(pattern, html)
    if match_results is not None:
        title = match_results.group()
        
        pattern1 = "courses/.*?/a>"
        prereqs = re.findall(pattern1, title)
        listofprereqs = []
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
        prereqs = re.findall(pattern1, title)
        listofprereqs = []
        for i in prereqs:
            i = i.split('>')[1] 
            i = i.split('<')[0]
            listofprereqs.append(i)
        print("Coreqs: " )
        print(listofprereqs)


webscrape("comp 273")

