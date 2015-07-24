__author__ = 'poke19962008'

import pymongo

try:
    con = pymongo.Connection(host="localhost", port="27017")
except:
    print("Connection error")

db = con['date']
