#! /usr/bin/python3
# import os

# make sure we can open the file before we begin the other work
# filename = "cvc_trigrams.csv"
file = open("cvc_trigrams.csv", "w")  # open file for (over)writing

# letter lists
vowels = ['a', 'e', 'i', 'o', 'u']
consonantsBegin = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'y',
                   'z']  # excludes c, q, x
consonantsEnd = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x',
                 'z']  # excludes c, q, y

# list of permutations that we don't want in the final list, e.g. are recognizable English words (or meaningful to me)
badWords = ["bad", "bag", "ban", "bar", "bat", "bed", "beg", "bet", "bib", "bid", "big", "bit", "bob", "bog", "bop",
            "bot", "bow", "box", "bud", "bug", "bum", "bun", "bus", "but", "dab", "dad", "dam", "dan", "den", "dew",
            "did", "dig", "dim", "dip", "dog", "don", "dot", "dub", "dud", "dug", "duh", "fad", "fag", "fap", "fig",
            "fin", "fir", "fob", "fog", "fur", "gap", "gem", "gif", "gig", "gin", "git", "god", "got", "gun", "had",
            "hah", "ham", "has", "hat", "heh", "hen", "her", "him", "hip", "his", "hit", "hub", "hud", "hug", "huh",
            "hum", "hun", "jim", "kek", "kid", "kik", "lad", "lag", "lap", "led", "leg", "let", "lid", "lip", "lug",
            "mat", "max", "med", "meg", "meh", "men", "met", "mew", "min", "mix", "mom", "mop", "mud", "mug", "mum",
            "nab", "nad", "nag", "net", "nib", "not", "now", "nug", "num", "nut", "pad", "pan", "peg", "pep", "pet",
            "pig", "pin", "pod", "pog", "pop", "pot", "pow", "pub", "pup", "put", "rad", "rag", "ram", "rap", "rat",
            "raw", "red", "rex", "rib", "rid", "rig", "rim", "rip", "rod", "rot", "row", "rub", "rug", "rum", "run",
            "sad", "sag", "sam", "set", "sew", "sex", "sim", "sin", "six", "sob", "sod", "sog", "sol", "son", "sow",
            "sub", "sud", "sun", "tab", "tad", "tag", "tan", "tap", "tax", "ted", "ten", "tim", "tin", "tip", "tit",
            "top", "tot", "tow", "tub", "tug", "tux", "vat", "wad", "wag", "wig", "wit", "wok", "wow", "yak", "yep",
            "yes", "yet", "yif", "yum", "zap", "zip"]

permutations = []  # list in which we'll be storing the permutations

# generate and store consonant-vowel-consonant trigram permutations
for a in consonantsBegin:
    for b in vowels:
        for c in consonantsEnd:
            permutations.append(a + b + c)

# remove permutations we don't want
for word in badWords:
    permutations.remove(word)

# write the permutations to the file
for entry in permutations:
    file.write(entry + '\n')

file.close()  # close file
