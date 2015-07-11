__author__ = 'poke19962008'

import urllib
from bs4 import BeautifulSoup
import re
import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
import json
from bson import BSON


# link = "http://en.wikipedia.org/wiki/List_of_countries_and_capitals_with_currency_and_language"
# html = urllib.urlopen(link)
# html_doc_w = open("html_doc.txt", "w")
# html_doc_w.write(html.read())


html_doc = file("html_doc.txt", "r")
soup = BeautifulSoup(html_doc.read())

for table_tags in soup.find_all('table'):
    if table_tags['class'] == ["wikitable", "sortable"] :
        africa_table = BeautifulSoup(table_tags.encode('utf-8'))
        break

count_link = list()
count_name = list()
flag = 0
for count_tag in africa_table.find_all('tr'):
    if flag == 0:
        flag = 1
        continue
    else:
        name_tag = BeautifulSoup(count_tag.encode('utf-8')).find_all('td')[1]
        name_href = "http://en.wikipedia.org" + BeautifulSoup(name_tag.encode('utf-8')).find('a')['href'].encode('utf-8')
        count_link.append(name_href)
        count_name.append(BeautifulSoup(name_tag.encode('utf-8')).find('a').string.encode('utf-8'))

        if count_name[len(count_name)-1] == "Kenya":     #Break in Kenya
            break

i=0
count_data = {}
for i in range(len(count_link)):         #itereate through the list of countries
    file_name = "%s.txt" % count_name[i]
    count_data[count_name[i]] = {}

    # html = urllib.urlopen(count_link[i])
    # html_doc_w = open(file_name, "w")
    # html_doc_w.write(html.read())

    html_doc = open(file_name, "r")
    soup = BeautifulSoup(html_doc.read())
    para = soup.find_all('p')
    header_list = []
    header_value_list = []

    for tag in soup.find_all('p'):
        if tag.b:
            count_data[count_name[i]]['Details'] = re.sub('\[[0-9]\]', '', BeautifulSoup(tag.encode('utf-8')).get_text().encode('utf-8')) #Insert intro paragraph
            break

    for tag in soup.find_all('table'):         #Find the infobox
        if tag['class'] == ['infobox', 'geography', 'vcard']:
            infobox_tag = tag
            break

    for tag in infobox_tag.tr.find_next_siblings('tr'):
        if (tag.get('class') == ['adr']) or (tag.get('style') == "font-size:85%;"):
            continue

        if tag.find_next().get('class') == ['maptable']:                         #Insert flag and emblem
            img_link = list()
            for img in tag.find_all('img'):
                img_link.append("http://" + img['src'].encode('utf-8')[2:])
            count_data[count_name[i]]['Flag'] = img_link[0]
            count_data[count_name[i]]['Emblem'] = img_link[1]
            continue


        header_data = ""
        header_value = ""
        header = True
        for row in tag.stripped_strings:
            if row == "-":
                header_data = header_data + row
                continue
            if header == True:                      #Header Value of the row
                header_data = header_data + row
                header = False
                continue

            header_value = header_value + row        #Table row data

        if header_value == "":
            header_value = "NA"
        if (header_data == "") or (header_data == "["):
            header_data = "NA"

        header_value_list.append(re.sub('\[[0-9]\]', '', header_value.encode('utf-8')))   #append into a single list removing [(0-9)]
        header_list.append(re.sub('\[[0-9]\]', '', header_data.encode('utf-8')))

    buff=""
    for j in range(len(header_list)-1):
        if (header_list[j+1][0] == "-") and (header_list[j][0] != "-"):
            buff = header_list[j]
        elif (header_list[j+1][0] != "-") and (header_list[j][0] != "-"):
            buff = ""

        if buff != "":
            if header_list[j][0] == "-":
                header_list[j] = buff + header_list[j]


    for j in range(len(header_value_list)):
        if (header_value_list[j] == "NA") or (header_list[j] == "Location of") or (header_list[j] == "NA"):
            continue
        header_list[j] = re.sub('\:', '', header_list[j])

        if header_list[j] == "Anthem":
            header_value_list[j] = re.sub('(Sorry, your browser either has JavaScript disabled or does not have any supported player.You candownload the clipordownload a playerto play the clip in your browser.)', '', header_value_list[j])

        count_data[count_name[i]][header_list[j]] = header_value_list[j]

    break
    i=i+1


# for name in count_data:     #txt format
#     file_name = "db_%s.txt" % name
#     file_ = open(file_name,  "a")
#
#     for key, value in count_data[name].items():
#         file_.write(str(key) + " : " + str(value) + "\n\n")


try:                                                                        #Connecting MongoDB
    con = Connection(host="localhost", port=27017)

    db_handler = con["SRM-SE"]
    assert db_handler.connection == con
    db_handler.SayanT3.insert(count_data, safe=True)
except ConnectionFailure, e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)



# file_ = open("count_db.json", 'w')                        #converting to JSON
# json.dump(count_data, file_, indent=4)

# file_ = open("count_db.bson", 'w')                        #converting to BSON
# bson_string = BSON.encode(count_data)
# file_.write(bson_string)





