__author__ = 'poke19962008'

'''
    what is the features of Vostro 14 V3446?
    what is the features of Vostro 14 V3446 Notebook?
    what is the feature of Vostro 14 V3446?
'''

import pymongo, json, sys
import keywordExtractor
key = ['feature', 'features', 'type', 'company', 'brand']

def main():
    try:
        con = pymongo.Connection(host="localhost", port=27017)
    except:
        print("Connection not successful ")
    dbh = con["electronics"]

    # string = " ".join(sys.argv[1:])
    query = keywordExtractor.extract("what is the features of Vostro 14 V3446?")
    what = [x for x in query if x in key]
    query.remove(what[0])
    model = " ".join(query)

    if what[0] in ['feature', 'features']:
        what = "features"
    elif what is 'type':
        what = what[0]
    elif what in ["company", 'brand']:
        what = "company"

    tuple = dbh.users.find_one({
                                    "model": {
                                        "$regex": model,
                                        "$options": "i"
                                    }
                                }
                               , {
                                    "_id": False,
                                    "model": True,
                                    what: True,
                                    "img src": True,
                                    "website link": True
                                  })
    print(tuple)

if __name__ == "__main__":
    main()