import requests
import sys
import webbrowser
import bs4

print('Googling...')
res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='html.parser')

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
