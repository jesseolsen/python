# Rename files in a directory

import os

list = os.listdir('./data')

#Add footer to each file in ./data directory
for file in list:
    src = "./data/" + file

    # Read file
    f = open(src, "r")
    content = f.read()

    # Write file
    f = open(src, "w")
    f.write("Header.\n")
    f.write(content)
    print("{}:\n{}\n\n".format(src, content))

