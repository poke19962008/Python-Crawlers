__author__ = 'poke19962008'

import mysql.connector
from bs4 import BeautifulSoup
import urllib2

db=mysql.connector.connect(user='root', host='localhost' , database='SRM_SE' , port=8888 )
cursor = db.cursor()

# f = open("index.html", "r").read()
# soup = BeautifulSoup(f)

soup = BeautifulSoup(urllib2.urlopen('www.URL.com').read())

for tag in soup.find_all('tr' , class_='club-row'):
    data={}
    for td in BeautifulSoup(tag.encode('utf-8')).find_all('td'):
        if td['class'][0]=='col-sort':
            key='IMG'
            value='null'
        else:
            key=td['class'][0].split('-')[1].upper()
            value=td.text
        data[key]=value

    insert_sql=("INSERT INTO `BARCLAYS` (LP , IMG , GF , CLUB , PTS , POS , L , P , GD , W , GA , D ) VALUES (%(LP)s, %(IMG)s, %(GF)s, %(CLUB)s, %(PTS)s, %(POS)s, %(L)s, %(P)s, %(GD)s, %(W)s, %(GA)s, %(D)s )")
    cursor.execute(insert_sql,data)
    db.commit()
db.close()




