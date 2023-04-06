from bs4 import BeautifulSoup, SoupStrainer
import requests

#url = "https://dr-stone.org/"

def grab_webtoon_chapter_links(url):
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data)
    list_of_links = []

    for link in soup.find_all('a'):
        if "https://dr-stone.org/manga/dr-stone-chapter-" in link.get('href'):
            list_of_links.append(link.get('href'))
            #print(link.get('href'))
    return list_of_links