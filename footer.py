# Rename files in a directory

import os

list = os.listdir('./data')

#Add header to each file in ./data directory
for file in list:
    src = "./data/" + file

    # Read file
    f = open(src, "r")
    content = f.read()

    # Append to file
    f = open(src, "a")
    f.write("Footer.\n")
    print("{}:\n{}\n\n".format(src, content))

