# Rename files in a directory

import os

print("Hello world!")

list = os.listdir('./data')

print("Initial List:")
for file in list:
    print(file)

for file in list:
    #rename
    src = "./data/" + file
    #dest = "./data/" + file + ".txt"
    #dest = src.replace(".text.txt", ".txt")
    #print("Rename from {} to {}".format(src, dest))
    dest = "dest"
    print("Rename from %s to %s" % (src, dest))
    #os.rename(src, dest)

    #with open(src, "r") as f:
    #    f.write("hi")

    #content = f.read()
    #f = open(src, "w")
    #f.write("The Beginning.\n")
    #f.write(content)
    #print("{}:\n{}\n\n".format(src, content))


list = os.listdir('./data')
print("Final List:")
for file in list:
    print(file)

