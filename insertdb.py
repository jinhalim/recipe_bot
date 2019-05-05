import json

myJson = {}

tempRecipe = open("C:/Users/jinhalim/Desktop/recipe_bot/dessert.txt","r")

i = 0
for line in tempRecipe.readlines():
    subline = line.split('\n')
    myJson[i] = subline[0].split('\t')
    print("insert into big_category values ("+myJson[i][0]+", '"+myJson[i][1]+"') ;")
    i += 1

# print(myJson)


tempRecipe.close()