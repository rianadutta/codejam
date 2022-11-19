from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.mcgill.ca/study/2022-2023/courses/math-248"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
pattern = '<li><p>Prerequisites:.*?/p>'
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
print(title)


