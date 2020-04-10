#!/usr/bin/python3
# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))
filename = "cyc_trigram.csv"

# os.remove(dir_path + "/" + filename)
# print("Existing file '" + filename + "' removed!")
file = open("cyc_trigram.txt", "w")    # open file for writing

# letter lists
consonantsBegin = ['b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
consonantsEnd = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']

# generate permutations
for a in consonantsBegin:
    for b in vowels:
        for c in consonantsEnd:
            file.write(a + b + c + "\n")

file.close()    # close file