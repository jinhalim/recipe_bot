import os
import json

seach = '&&'
seach1 = '**'
def textlist(f,newtext):
    list1 = []
    for line in f.readlines():
        line1 = line.split('\n')
        # # print(f.readline())
        if(line1[0] in seach):
            # print(list1)
            newtext.writelines(list1)
            # newtext.writelines('\n')
            list1 = []
            list1.append(line1[0])
        else:
            list1.append(line1[0])


i = 0
for root, subdirs, files in os.walk('./please_v2'):
    for file in files:
        with open("./please_v2/"+file, 'r') as f:
            i += 1
            s = str(i)
            newtext = open("./please_v2/"+s+".txt", 'w')
            textlist(f,newtext)
            


