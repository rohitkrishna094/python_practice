import requests
import sys
import webbrowser
import bs4

url = 'https://www.google.com/'


def getLinks(link):
    print(link)
    res = requests.get(link)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    ls = soup.find_all('a')
    links.extend(ls)
    links.remove(link)
    visited_links.add(link)
    return ls


visited_links = set([])
links = [url]
res = getLinks(url)

i = 0
while len(links) != 0:
    getLinks(links[i])
    i = i + 1

print(len(visited_links), len(links))
