import json

myJson = {}

tempRecipe = open("C:/Users/jinhalim/Desktop/국물.txt","r")
myNewfile = open("C:/Users/jinhalim/Desktop/뉴국물.txt","w")
counter = 0

for line in tempRecipe.readlines():
    myNewfile.writelines(line.strip())

tempRecipe.close()
myNewfile.close()