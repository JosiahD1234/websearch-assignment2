import requests
from bs4 import BeautifulSoup
import re

def crawler(seed):
    frontier = [seed]
    seen = set()
    seen.add(seed)
    while frontier:
        url = frontier.pop(-1)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        print(soup.h1.get_text())
        links = extract_links(soup)
        convert_to_absolute_url(links, url)
        for link in links:
            if not link in seen and bool(re.match(r"^https://testingurl.dev/scraping/links/circular", link)):
                seen.add(link)
                frontier.append(link)
    return seen

def extract_links(soup):
    links = soup.find_all('a')
    for i, link in enumerate(links):
        links[i] = link.get('href')
    return links

def convert_to_absolute_url(links, url):
    for i, link in enumerate(links):
        if bool(re.match(r"^/.*", link)):
            # I found this regex online to extract the domain
            links[i] = re.search(r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)", url).group() + link

results = crawler("https://testingurl.dev/scraping/links/circular")
for result in results:
    print(result)