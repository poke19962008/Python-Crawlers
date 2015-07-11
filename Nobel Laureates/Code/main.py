__author__ = 'poke19962008'

import urllib
from bs4 import BeautifulSoup
import re
import json
from bson import BSON

# url = "http://www.nobelprize.org/nobel_prizes/physics/laureates/"
# html = urllib.urlopen(url)
# file_w = open("html.txt", "w")
# file_w.write(html.read())

# file_r = open("html.txt", "r")
# html = file_r.read()
#
# soup = BeautifulSoup(html)
# year_tag = soup.find_all("div", class_="by_year")

# year_list = []
# for tag in year_tag:
#     year_url = "http://www.nobelprize.org"+tag.h3.a['href'].encode('utf-8')
#     html = urllib.urlopen(year_url)
#
#     soup = BeautifulSoup(html.read())
#
#     title_string = soup.head.title.string.encode('utf-8')
#     comp = re.compile("[0-9]")
#     year = comp.findall(title_string)
#     year = "".join(year)
#     year_list.append(year)
#     file_name = "%s.txt" % year

    # file_w = open(file_name, 'w')
    # html = urllib.urlopen(year_url)
    # file_w.write(html.read())


# file_w = open("Year List.txt", "w")
# file_w.write("#".join(year_list))

file_r = open("Year List.txt", "r")
year_list = file_r.read().split("#")

data = {}
for year in year_list:
    file_name = "%s.txt" % year
    file_r = open(file_name, "r")

    soup = BeautifulSoup(file_r.read())
    tag = soup.find('div', class_="prize_wrapper")
    tag = tag.div
    soup = BeautifulSoup(tag.encode('utf-8'))

    for tag in soup.find_all('div', class_="large-4 columns"):
        if tag.a != None:
            link = "http://www.nobelprize.org/nobel_prizes/physics/laureates/" + year + "/" + tag.a['href'].encode('utf-8')
        else:
            continue
        name = tag.h3.text.encode('utf-8')
        id = tag.a.img['src'].encode('utf-8')

        data[name] = {}
        data[name]['id'] = id
        data[name]['date'] = year

        html = urllib.urlopen(link)
        soup_ = BeautifulSoup(html.read())

        info_tag = soup_.find('div', class_="laureate_info_wrapper")
        info_tag = info_tag.div

        for tag in info_tag.find_all('p')[1:-1]:
            if tag.strong != None:
                if tag.strong.text == "Born:":
                    data[name]['born'] = tag.span.text.encode('utf-8')
                    data[name]['country'] = re.sub(tag.strong.text.encode('utf-8') + " " + tag.span.text.encode('utf-8'), "",tag.text.encode('utf-8'))[2:]
                elif tag.strong.text == "Affiliation at the time of the award:":
                    data[name]['affiliation_institution'] = tag.span.text.encode('utf-8')

                elif tag.strong.text == "Prize motivation:":
                    data[name]['prize_reasearch'] = tag.text.encode('utf-8').split("\"")[1]

                elif tag.strong.text == "Field:":
                    data[name]['field'] = re.sub("Field: ", "", tag.text.encode('utf-8'))
        print(data[name])


file_ = open("Nobel_Laureates_db.json", 'w')                        #converting to JSON
json.dump(data, file_, indent=4)

file_ = open("Nobel_Laureates_db.bson", 'w')                        #converting to BSON
bson_string = BSON.encode(data)
file_.write(bson_string)