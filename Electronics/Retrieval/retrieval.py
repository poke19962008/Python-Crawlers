__author__ = 'poke19962008'

'''
    what are the features of Vostro 14 V3446?
    what are the features of Vostro 14 V3446 Notebook?
    what are the feature of Vostro 14 V3446?
    what are the features of Dell Vostro? <---- Return multiple matching results
'''

import pymongo, json
import keywordExtractor
key = ['feature', 'features', 'type', 'company', 'brand']

def main():
    try:
        con = pymongo.Connection(host="localhost", port=27017)
    except:
        print("Connection not successful ")
    dbh = con["electronics"]

    query = keywordExtractor.extract("what are the features of Samsung Galaxy camera?")
    what = [x for x in query if x in key]
    query.remove(what[0])
    model = " ".join(query)

    if what[0] in ['feature', 'features']:
        what = "features"
    elif what is 'type':
        what = what[0]
    elif what in ["company", 'brand']:
        what = "company"

    company = dbh.users.find_one({
                                "company": {
                                    "$regex": model.split()[0],
                                    "$options": "i"
                                }
                            }
                        ,  {
                                "company": True
                            }
    )

    if company != None:
        model = " ".join(model.split()[1:])

    tuple = dbh.users.find({
                                    "model": {
                                        "$regex": model,
                                        "$options": "i"
                                    }
                                }
                               , {
                                    "_id": False,
                                    "model": True,
                                    "company": True,
                                    what: True,
                                    "img src": True,
                                    "website link": True
                                  })
    print("Results Found: " , tuple.count())
    for i in range(tuple.count()):
        print(tuple[i])

if __name__ == "__main__":
    main()