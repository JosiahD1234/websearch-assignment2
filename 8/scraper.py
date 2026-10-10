#-------------------------------------------------------------------------
# AUTHOR: Josiah Degeneffe
# FILENAME: scraper.py
# SPECIFICATION: A web scraper that crawls through the circular links on testingurl.dev
# FOR: CS 4250 - Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup
import re

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
# --> add your Python code here
frontier = [seed]
seen = set()
seen.add(seed)

# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    # --> add your Python code here
    url = frontier.pop(-1)

    # Retrieving and parsing the Web page
    # --> add your Python code here
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    # Printing the text contained in the <h1> element
    # --> add your Python code here
    print(soup.h1.get_text())

    # Extracting and processing hyperlinks
    # --> add your Python code here
    links = soup.find_all('a')
    for i, link in enumerate(links):
        links[i] = link.get('href')
        if bool(re.match(r'^/', links[i])):
            links[i] = baseURL + links[i]
    for link in links:
        if not link in seen and bool(re.match(r'^https://testingurl.dev/scraping/links/circular', link)):
            frontier.append(link)
            seen.add(link)

# Printing all URLs in seen
# --> add your Python code here
for link in seen:
    print(link)