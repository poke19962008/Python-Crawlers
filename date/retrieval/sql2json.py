__author__ = 'poke19962008'

import  re, json

def convert(keys, filename):
    # keys = ['url', 'loc', 'country', 'time', 'latlong', 'currency', 'language', 'phonecode', 'weather', 'image', 'others']

    file_ = open(filename + '.json', 'a')

    with open(filename + '.sql', 'r') as f:
        for data in f.readlines():
            values = data.split("\',")
            data = {}

            for i in range(len(keys)):
                try:
                    data[keys[i]] = re.sub(r"\'|:|\"|\(|\),|\n", "", values[i])
                except:
                    print("Cannot write: ")
                    print("Index=", i, keys[i], "\n" ,data)

            json.dump(data, file_)
            file_.write("\n")

def main():

    print("Converting from SQL to JSON")
    convert(['url', 'loc', 'country', 'time', 'latlong', 'currency', 'language', 'phonecode', 'weather', 'image', 'others'], 'date_mod')
    print("Finished...")

if __name__ == '__main__':
    main()