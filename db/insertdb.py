import json

myJson = {}

tempRecipe = open("C:/Users/jinhalim/Desktop/recipe_bot/dessert.txt","r")

i = 0
count = 900
for line in tempRecipe.readlines():
    subline = line.split('\n')
    myJson[i] = subline[0]
    count += 1
    count_1 = str(count)
    print("insert into big_category values ("+ count_1 +", '"+subline[0]+"') ;")
    i += 1

# print(myJson)


tempRecipe.close()