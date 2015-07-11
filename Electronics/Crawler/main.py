__author__ = 'poke19962008'

import mysql.connector
from bs4 import BeautifulSoup
import urllib2, re, json

db = mysql.connector.connect(user='root', host='localhost', database = 'brainse', port=8888)
cursor = db.cursor()


links = {"http://www.buyingiq.com/s/laptops/": 51}                  #{ <link> : <max pages> }
products = []

table_sql = ( "CREATE TABLE `ELEC` (SNO INT(200) PRIMARY KEY, TYPE VARCHAR(200), COMPANY VARCHAR(200), MODEL VARCHAR(200), FEATURES VARCHAR(200), WEBSITE VARCHAR(200), IMG VARCHAR(200) )")
insert_sql = ("INSERT INTO `ELEC` (SNO, TYPE, COMPANY, MODEL, FEATURES, WEBSITE, IMG) VALUES (%(SNO)s, %(TYPE)s, %(COMPANY)s, %(MODEL)s, %(FEATURES)s, %(WEBSITE)s, %(IMG)s)")

cursor.execute(table_sql)

key=0
for link in links:                                                  # <link>
    limit = links[link]
    type = link.split("/")[4:-1][0]

    for page_no in range(limit+1):                                  # <link>/<page_no>
        link_ = link + str(page_no)
        soup = BeautifulSoup(urllib2.urlopen(link_).read())
        soup = BeautifulSoup(soup.find('div', class_='result-row clearfix').encode('utf-8'))

        for item in soup.find_all('div', class_='filter-result'):
            soup_ = BeautifulSoup(item.encode('utf-8'))

            key = key + 1

            img_src = soup_.find('div', class_='result-img').img['data-srcset']                                             # image source

            result_details_div = soup_.find('div', class_='result-details')
            website_link = "http://www.buyingiq.com" + result_details_div.a['href'].encode('utf-8')                 # website link

            model = re.sub(r'\((.*)\)', "", " ".join(result_details_div.a['title'].encode('utf-8').split(" ")[:-4]))# model [Dell Vostro 14 V3446 Notebook (4th Gen Ci3/ 4GB/ 500GB/ Ubuntu/ 2GB Graph) Price, Reviews and Specs --->  Dell Vostro 14 V3446 Notebook]
            model_ = model
            model = " ".join(model.split(" ")[1:])

            result_keyfeatures_div = BeautifulSoup(result_details_div.find('div', class_='result-keyfeatures').encode('utf-8'))

            features = []
            for tag in result_keyfeatures_div.find_all('li'):                                                        # Features
                features.append(tag.span.text)                                                                       # <feature1>||<feature2>||..... We can further use split

            if type == "laptops":
                company = model_.split(" ")[0]

            products.append({'key': key, 'type': type, 'company': company, 'model': model, 'features': features, 'website link': website_link, 'img src': img_src})

            cursor.execute(insert_sql, {'SNO': int(key), 'TYPE': type, 'COMPANY': company, 'MODEL': model, 'FEATURES': "||".join(features), 'WEBSITE': website_link, 'IMG': img_src})

            print(model + " done!!!")
            db.commit()

#file_ = open("db.json", "w")
#json.dump(products, file_, indent=4)

db.close()
