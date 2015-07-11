__author__ = 'poke19962008'

from bs4 import BeautifulSoup
import mysql.connector
import urllib
import re


html_doc_w = open("html_doc.txt", "w")
html_doc = open("html_doc.txt", "r")


url = "http://en.wikipedia.org/wiki/State_Bank_of_India"
html_doc_w.write(urllib.urlopen(url).read())

db = mysql.connector.connect(user='root', host='localhost', database = 'SRM_SE')
cursor = db.cursor()

html_soup = BeautifulSoup(html_doc.read())

for table_tag in html_soup.find_all('table'):
    if table_tag['class'] == ['infobox', 'vcard']:
        infobox_soup = BeautifulSoup(table_tag.encode('utf-8'))
        tr_soup = BeautifulSoup(table_tag.encode('utf-8'))


header = html_soup.caption.string.encode('utf-8')
file_name = "%s_dict.txt" % header
dict_db = open(file_name, "w")

row_num = 0
attr = "Img Url#"

for tr_tag in tr_soup.find_all('tr'):
    if row_num != 0:
        th_soup = BeautifulSoup(tr_tag.th.encode('utf-8'))

        for th_tag in th_soup.strings:
            _attr_ = re.sub('[\n]', '', th_tag.encode('utf-8'))
            attr = attr + _attr_ + "#"

    row_num = row_num + 1

attr = attr.split("#")
attr = filter(None, attr)

attr_val = "http:/" + infobox_soup.tr.td.img['src'].encode('utf-8')[1:]
for table_row in infobox_soup.find_all('tr'):

    attr_val_ = ""

    for td in table_row.td.stripped_strings:
        if table_row.th == None :
            continue

        if table_row.th.get_text() == "Website":
            attr_val_ = table_row.td.a['href'].encode('utf-8')
            break
        else:
            attr_val_ = attr_val_ + td.encode('utf-8') + " "

    attr_val_ = re.sub('\[ [0-9] ]', '', attr_val_)
    attr_val = attr_val + attr_val_ + "#"

attr_val = filter(None, attr_val.split("#"))

for i in range(len(attr)):
    dict_db.write(attr[i] + ": " + attr_val[i] + '\n')


table_sql = ( "CREATE TABLE `"+ str(header) +"` (HEADER VARCHAR(200), VALUE VARCHAR(200))")
cursor.execute(table_sql)

insert_sql = ("INSERT INTO `"+ str(header) +"` (HEADER, VALUE) VALUES (%(HEADER)s, %(VALUE)s)")

i=0
for i in range(len(attr)):
    cursor.execute(insert_sql, {'HEADER': attr[i], 'VALUE': attr_val[i]})

db.commit()
db.close()