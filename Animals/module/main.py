__author__ = 'poke19962008'

from nltk import pos_tag                                                                                                # """ Paste the json files from 'db' to pwd """
import re, pymongo,json, os, time

start_time = time.time()

animals = ['Monte Iberia Eleuth', 'Tasmanian Devil', 'Albatross', 'Tortoise', 'Butterfly', 'Galapagos Tortoise', 'Spider Monkey', 'Howler Monkey', 'Lobster', 'Electric Eel',
           'Royal Penguin', 'Woodpecker', 'Pied Tamarin', 'Weasel', 'Tang', 'Stellers Sea Cow', 'Indian Elephant', 'Yak', 'Arctic Hare', 'Avocet', 'Clown Fish', 'Barnacle',
           'Cheetah', 'Dugong', 'Caiman', 'Sea Slug', 'Barb', 'Indri', 'Marsh Frog', 'Aye Aye ', 'Bactrian Camel', 'South China Tiger', 'Leopard Tortoise', 'Wild Boar', 'Frigatebird',
           'Seal', 'Pademelon', 'Capybara', 'Wolverine', 'King Penguin', 'Asian Giant Hornet', 'Bottle Nosed Dolphin', 'Guinea Pig', 'Elephant Seal', 'Leopard', 'Spectacled Bear',
           'Adelie Penguin', 'Ibis', 'Hammerhead Shark', 'Borneo Elephant', 'Black Widow Spider', 'Numbat', 'Pond Skater', 'Molly', 'Chicken', 'Gopher', 'Bat', 'Panther', 'Gorilla',
           'Wallaby', 'Stoat', 'Tuatara', 'Stick Insect', 'Komodo Dragon', 'Pink Fairy Armadillo', 'Axolotl', 'Squirrel Monkey', 'Aldabra Giant Tortoise', 'Markhor', 'Bull Shark',
           'Bornean Orangutan', 'Siamese Fighting Fish', 'Sheep', 'Dolphin', 'Mountain Lion', 'Quokka', 'African Tree Toad', 'Clouded Leopard', 'Sea Squirt', 'Indian Palm Squirrel',
           'Zebra Shark', 'Heron', 'Horn Shark', 'Lionfish', 'Porcupine', 'Baboon', 'Brown Bear', 'Indian Rhinoceros', 'Cat', 'Barn Owl', 'Chimpanzee', 'Jackal', 'Okapi', 'Puss Moth',
           'Tiger', 'Tiger Salamander', 'Tarsier', 'Rhinoceros', 'Serval', 'Hedgehog', 'Quetzal', 'Leopard Seal', 'Puma', 'Gharial', 'Woodlouse', 'Javan Rhinoceros', 'Grey Mouse Lemur',
           'Fire Bellied Toad', 'Great White Shark', 'Manta Ray', 'Angelfish', 'Scorpion Fish', 'Crane', 'Toucan', 'Impala', 'Red handed Tamarin', 'Gar', 'Siberian Tiger', 'Emperor Penguin',
           'Vervet Monkey', 'Woolly Mammoth', 'Chinchilla', 'African Bush Elephant', 'Asian Palm Civet', 'Anteater', 'Lizard', 'Vampire Bat', 'Crested Penguin', 'Honey Bee', 'Gerbil', 'Piranha',
           'Raccoon', 'Dodo', 'Llama', 'Penguin', 'Booby', 'Red Panda', 'Sperm Whale', 'Patas Monkey', 'Emu', 'Dingo', 'Roseate Spoonbill', 'Pelican', 'Insect', 'Tetra', 'Chipmunk',
           'Crocodile', 'Arctic Fox', 'Kangaroo', 'Falcon', 'Puffer Fish', 'Hamster', 'Moth', 'Meerkat', 'Water Dragon', 'Dhole', 'Bearded Dragon', 'African Civet', 'Flying Squirrel',
           'Cuscus', 'Butterfly Fish', 'Coral', 'Grasshopper', 'Crab', "Darwin's Frog", 'Prawn', 'Walrus', 'Sand Lizard', 'Red Wolf', 'Beetle', 'Skunk', 'Ant', 'Grizzly Bear', 'Macaw',
           'Zonkey', 'Wombat', 'Caiman Lizard', 'Malayan Tiger', 'Warthog', 'Orangutan', 'Elephant Shrew', 'Common Loon', 'Monkey', 'Manatee', 'Magpie', 'Sea Urchin', 'Horseshoe Crab',
           'Minke Whale', 'Parrot', 'Bonobo', 'Donkey', 'Badger', 'Asian Elephant', 'Snail', 'Cross River Gorilla', 'Frilled Lizard', 'Saola', 'Cockroach', 'Gila Monster', 'Moorhen',
           'Sumatran Rhinoceros', 'Sea Dragon', 'Sparrow', 'Neanderthal', 'Wildebeest', 'Human', 'Leopard Cat', 'Wrasse', 'Snowy Owl', 'Glass Lizard', 'Moray Eel', 'Cuttlefish',
           'Jaguar', 'Blue Whale', 'Rock Hyrax', 'Gibbon', 'Tawny Owl', 'Monitor Lizard', 'Otter', 'Cichlid', 'Fennec Fox', 'Mongoose', 'Sea Lion', 'Bobcat', 'Catfish', 'Pika',
           'Hummingbird', 'Koala', 'Rabbit', 'Dormouse', 'Possum', 'Sponge', 'Chinstrap Penguin', 'Leaf Tailed Gecko', 'Desert Tortoise', 'Scorpion', 'Raccoon Dog', 'Reindeer',
           'Alligator', 'Long Eared Owl', 'XRay Tetra', 'Ostrich', 'Proboscis Monkey', 'Ocelot', 'Woolly Monkey', 'African Penguin', 'Oyster', 'Quoll', 'Moose', 'Indochinese Tiger',
           'Galapagos Penguin', 'Grey Seal', 'Dwarf Crocodile', 'Beaver', 'Giant Panda Bear', 'Starfish', 'Hercules Beetle', 'Fly', 'Goat', 'Hippopotamus', 'African Wild Dog',
           'Radiated Tortoise ', 'African Forest Elephant', 'Tropicbird', 'Thorny Devil', 'Black Bear', 'Caterpillar', 'White Faced Capuchin', 'Dog', 'Wolf', 'Giant African Land Snail',
           'Armadillo', 'White Rhinoceros', 'Collared Peccary', 'Golden Lion Tamarin', 'Bengal Tiger', 'Fin Whale', 'Bandicoot', 'Mountain Gorilla', 'Newt', 'Guppy', 'Spadefoot Toad',
           'Magellanic Penguin', 'Chameleon', 'Pike', 'Sea Turtle', 'Robin', 'Common Toad', 'Polar Bear', 'Basking Shark', 'Echidna', 'Duck', 'Little Penguin', 'Poison Dart Frog',
           'Gentoo Penguin', 'Ladybird', 'Dragonfly', 'Bongo', 'Termite', 'Yellow Eyed Penguin', 'Nightingale', 'Fishing Cat', 'Pool Frog', 'Keel Billed Toucan', 'Zebu', 'Macaroni Penguin',
           'Buffalo', 'Golden Oriole', 'Sun Bear', 'Opossum', 'Sumatran Tiger', 'Marine Toad', 'Humboldt Penguin', 'Wasp', 'Chamois', 'Tiger Shark', 'Rat', 'Edible Frog', 'Malayan Civet',
           'Tree Frog', 'Sri Lankan Elephant', 'Mandrill', 'Binturong', 'Eagle', 'African Clawed Frog', 'Sumatran Orangutan', 'Dusky Dolphin', 'Puffin', 'Seahorse', 'Masked Palm Civet',
           'Quail', 'Horse', 'Camel', 'Banded Palm Civet', 'Budgerigar', 'Mole', 'Highland Cattle', 'Bumble Bee', 'Guinea Fowl', 'Common Buzzard', 'Lynx', 'Sumatran Elephant', 'Liger',
           'Lemming', 'Elephant', 'Geoffroys Tamarin', 'Frog', 'Shrimp', 'Rockhopper Penguin', 'Lion', 'Swan', 'Sea Otter', 'Coati', 'Grouse', 'Uguisu', 'Kudu', 'Japanese Macaque',
           'Western Lowland Gorilla', 'Grey Reef Shark', 'Pig', 'Uakari', 'Vulture', 'Killer Whale', 'Pheasant', 'Squirrel', 'Hare', 'Nurse Shark', 'Eastern Gorilla', 'Birds Of Paradise',
           'Zebra', 'Cottontop Tamarin', 'Sloth', 'Iguana', 'Gecko', 'Green Bee Eater', 'Flamingo', 'Antelope', 'Hyena', 'Pygmy Marmoset', 'River Dolphin', 'Sabre Toothed Tiger', 'Mayfly',
           'Silver Dollar', 'Giraffe', 'Snake', 'Zorse', 'Goose', 'Western Gorilla', 'Burrowing Frog', 'Kiwi', 'Bullfrog', 'Hermit Crab', 'Coyote', 'Arctic Wolf', 'River Turtle', 'Squid',
           'Kingfisher', 'Giant Clam', 'Lemur', 'Slow Worm', 'Water Vole', 'Peacock', 'Humpback Whale', 'Purple Emperor', 'White Tiger', 'Snapping Turtle', 'African Palm Civet',
           'Emperor Tamarin', 'Turkey', 'Ferret', 'Caracal', 'Stag Beetle', 'Fox', 'Whale Shark', 'Tapir', 'Stingray', 'Bear', 'Eastern Lowland Gorilla', 'Mule', 'Discus', 'Barracuda',
           'Octopus', 'Kakapo', 'Asiatic Black Bear', 'Jellyfish', 'Umbrellabird', 'Millipede', 'Mouse', 'Deer', 'King Crab', 'Flounder', 'Pygmy Hippopotamus', 'Black Rhinoceros', 'Fossa',
           'Horned Frog', 'Glow Worm', 'Striped Rocket Frog', 'Salamander', 'Water Buffalo', 'Red Knee Tarantula', 'Earwig ', 'Platypus', 'Olm', 'Bison', 'Spiny Dogfish', 'Fur Seal', 'Centipede']

string = "what is the Common Name of zorse "                     #Query Statement

tagged = pos_tag(string.split())

comp = []
for i in range(len(tagged)):                                #Extract all nouns and adjectives
    if re.search("NN|JJ|NNP|NNS|NNPS", tagged[i][1]):
        comp.append([tagged[i], i])
print("Query Skeleton: " +  str(comp) + "\n")               #Skeleton Syntax:[ [ (<word>, <Noun i.e.NN, Adjective i.e.JJ>), <position> ], ..... ]

break_outer = False
for i in range(len(comp)):                                  #Seperate the 'animal'
    for j in range(len(animals)):
        animal = animals[j].split(" ")

        flag = False
        for k in range(0,len(animal)):
            if comp[i+k][0][0].lower() != animal[k].lower():
                flag = True
                break
        if flag is False:
            animal = {"name": animals[j], "start": comp[i][1], "end": comp[i+len(animal)-1][1]}
            break_outer = True
            break
    if break_outer == True:
        break

query = []
for i in range(len(comp)):                                  #seperate the 'query'
    if (animal['start'] > comp[i][1]) or (animal['end'] < comp[i][1]):
        query.append(comp[i][0][0])
query = ' '.join(query)

print("query = " + query + "\nanimal = " + animal["name"] + "\n")

c = pymongo.Connection(host='localhost', port=27017)
db = c['Animal_Module']

# for i in range(len(animals)):                             #Make collections with Animal Names
#     file_name = "%s.json" % animals[i]
#     with open(file_name, 'r') as file_:
#         data = json.load(file_)
#
#     file_ = open(file_name, "a")
#     for key in data.keys():
#         dict_ = {}
#         dict_[key] = data[key]
#         db.collection[animals[i]].insert(dict_)

answer = list(db.collection[animal["name"]].find({query: {'$exists': True}}, { "_id": False, query: True}))
print("Answer: " + str(answer[0].values()[0]) + "\n")

print("Execution time: %s sec" % (time.time() - start_time))
