from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F_%D0%A1%D1%82%D0%B8%D0%B2%D0%B5%D0%BD%D0%B0_%D0%9A%D0%B8%D0%BD%D0%B3%D0%B0"
page = urllib.request.urlopen(url)

stephen_king_page = BeautifulSoup(page, "html.parser").find_all("table", class_="wikitable")[1]

def get_novels_links():
  links = stephen_king_page.find_all("a", href=True)
  wiki_url = "https://ru.wikipedia.org"
  filtered_links = list(filter(lambda link: link["href"].startswith("/wiki"), links))
  return list(map(lambda x: wiki_url + x["href"], filtered_links))

def get_parsed_novel(novels):
    for novel in novels:
        novel_link = urllib.request.urlopen(novel)
        novel_page = BeautifulSoup(novel_link, "html.parser")
        novel_content = novel_page.find("p")
        print(novel_content)

get_parsed_novel(get_novels_links())

