#!/usr/bin/python3
# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))
filename = "cyc_trigram.csv"

# os.remove(dir_path + "/" + filename)
# print("Existing file '" + filename + "' removed!")
file = open("cyc_trigram.csv", "w")  # open file for writing

# letter lists
consonantsBegin = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'y', 'z']  # exludes c, q, x
vowels = ['a', 'e', 'i', 'o', 'u']
consonantsEnd = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']  # excludes c, q, y

# list of purmations that we don't want in the final list, e.g. are recognizable English words
badWords = ["bad", "bag", "ban", "bar", "bat", "bed", "beg", "bet", "bib", "bid", "big", "bit", "bob", "bog", "bop", "bot", "bow", "box", "bud", "bug", "bum", "bun", "bus", "but", "dab", "dad", "dam", "dan", "den", "dew", "did", "dig", "dim", "dip", "dog", "don", "dot", "dub", "dud", "dug", "duh", "fad", "fag", "fap", "fig", "fin", "fir", "fob", "fog", "fur", "gap", "gem", "gif", "gig", "gin", "git", "god", "got", "gun", "had", "hah", "ham", "has", "hat", "heh", "hen", "her", "him", "hip", "his", "hit", "hub", "hud", "hug", "huh", "hum", "hun", "jim", "kek", "kid", "kik", "lad", "lag", "lap", "led", "leg", "let", "lid", "lip", "lug", "mat", "max", "med", "meg", "meh", "men", "met", "mew", "min", "mix", "mom", "mop", "mud", "mug", "mum", "nab", "nad", "nag", "net", "nib", "not", "now", "nug", "num", "nut", "pad", "pan", "peg", "pep", "pet", "pig", "pin", "pod", "pog", "pop", "pot", "pow", "pub", "pup", "put", "rad", "rag", "ram", "rap", "rat", "raw", "red", "rex", "rib", "rid", "rig", "rim", "rip", "rod", "rot", "row", "rub", "rug", "rum", "run", "sad", "sag", "sam", "set", "sew", "sex", "sim", "sin", "six", "sob", "sod", "sog", "sol", "son", "sow", "sub", "sud", "sun", "tab", "tad", "tag", "tan", "tap", "tax", "ted", "ten", "tim", "tin", "tip", "tit", "top", "tot", "tow", "tub", "tug", "tux", "vat", "wad", "wag", "wig", "wit", "wok", "wow", "yak", "yep", "yes", "yet", "yif", "yum", "zap", "zip"]

permutations = []  # list we'll be storing the permutations in

# generate permutations
for a in consonantsBegin:
    for b in vowels:
        for c in consonantsEnd:
            permutations.append(a + b + c)

# remove permutations we don't want
for word in badWords:
    permutations.remove(word)

for entry in permutations:
    file.write(entry + '\n')

file.close()  # close file