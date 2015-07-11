__author__ = 'poke19962008'

from bs4 import BeautifulSoup
import re,pymongo, urllib2, json
from bson import BSON

url = "http://a-z-animals.com/animals/scientific/"
html = urllib2.urlopen(url).read()
#
# file_w = open("html.txt", 'w')
# file_w.write(html.read())

# file_r = open("html.txt", 'r')
# html = file_r.read()

soup = BeautifulSoup(html)
table_tag = soup.find('table', class_='article_az')
table_soup = BeautifulSoup(table_tag.encode('utf-8'))

link = []
for tr_tag in table_soup.find_all('tr'):
    for td_tag in BeautifulSoup(tr_tag.encode('utf-8')).find_all('td'):
        for li_tag in BeautifulSoup(td_tag.ul.encode('utf-8')).find_all('li'):
            link.append("http://a-z-animals.com" + li_tag.a['href'].encode('utf-8'))

final_data = {}
for link in link:
    html = urllib2.urlopen(link).read()

    # file_r = open("sample.txt", "r")
    # html = file_r.read()
    soup = BeautifulSoup(html)

    name = soup.head.title.text.encode('utf-8')
    name = name.split("(")[0]
    final_data[name] = {}

    table = soup.find('table', class_="stretchy_content_hover")
    tr_tag = BeautifulSoup(table.encode('utf-8')).find_all('td')
    img = tr_tag[1].a.img['src'].encode('utf-8')
    final_data[name]['img'] = img

    table = soup.find('table', class_="article_facts")
    for tr_tags in BeautifulSoup(table.encode('utf-8')).find_all('tr'):
        header = tr_tags.td.text.split(":")[0]

        if header == "":
            continue

        data = BeautifulSoup(tr_tags.encode('utf-8')).find_all('td')[1].text
        final_data[name][header] = data
    print(name + " Done !!!")



file_ = open("Animals_db.json", 'w')                        #converting to JSON
json.dump(final_data, file_, indent=4)

file_ = open("Animals_db.bson", 'w')                        #converting to BSON
bson_string = BSON.encode(final_data)
file_.write(bson_string)

