from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F_%D0%A1%D1%82%D0%B8%D0%B2%D0%B5%D0%BD%D0%B0_%D0%9A%D0%B8%D0%BD%D0%B3%D0%B0"
page = urllib.request.urlopen(url)

stephen_king_page = BeautifulSoup(page, "html.parser").find_all("table", class_="wikitable")[1]

def get_novels_links():
  wiki_url = "https://ru.wikipedia.org"
  pick_href = lambda a: a["href"]
  add_prefix = lambda href: wiki_url + href
  pick_second_td = lambda tr_tag: tr_tag.find_all('td')[1]
  pick_first_a = lambda tag: tag.find('a')

  second_columns = map(pick_second_td, stephen_king_page.find_all('tr')[1:])
  links = filter(lambda x: x is not None, map(pick_first_a, second_columns))
  hrefs = map(pick_href, links)
  return list(map(add_prefix, hrefs))

def get_parsed_novel(novels):
  for novel in novels:
      novel_link = urllib.request.urlopen(novel)
      novel_page = BeautifulSoup(novel_link, "html.parser")
      novel_content = novel_page.select_one(".mw-parser-output > p").text
      result = re.sub(r'\([^)]*\)', '', novel_content, 1)
      result = re.sub(r'\[[^]]*\]', '', result)
      print(result)

get_parsed_novel(get_novels_links())