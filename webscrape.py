from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.mcgill.ca/study/2022-2023/faculties/science/undergraduate/programs/bachelor-science-bsc-major-computer-science"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
pattern = 'li class="program-course">*a>'
match_results = re.search(pattern, html, re.IGNORECASE)
#print(html)
title = match_results.group()

print(title)