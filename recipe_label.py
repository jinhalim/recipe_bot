import os


def textlist(f):
    for line in f:
        print(f.readline())

i = 0
for root, subdirs, files in os.walk('./please_v2'):
    for file in files:
        with open("./please_v2/"+file, 'r') as f:
            i += 1
            s = str(i)
            textlist(f)
            newtext = open("./please_v2/"+s+".txt", 'w')
            


