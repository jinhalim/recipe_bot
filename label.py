import json
import os
def check_list(li1):
    j = 0
    for j in li1:
        if(len(li1) <= j+1 or li1[j+1] == ""):
            print(li1[j],end = "\n")
            # print(li1[j+1],end = "\n")
            break
        else:
            print(li1[j],end = ",")

class Recipe :
    def __init__(self):
        self.name = []
        self.food1 = []
        self.food2 = []
        self.food3 = []
    def getall(self):
        return ["##",self.name] + ["&&",self.food1] + ["&&",self.food2] +["&&",self.food3]
        # return ["제목"]+[self.name] +["재료"]+ [self.food1] +["육수"]+ [self.food2] +["양념"]+[self.food3]

    def print_all(self):
        print(self.name)
        print(self.food1)
        print(self.food2)
        print(self.food3)

    def insert_list(self,li1,bt1,bt2,bt3,b4):
        if(bt1 == True):
            self.name.append(li1)
        elif(bt2 == True):
            self.food1.append(li1)
            self.food1.append(",")
        elif(bt3 == True):
            self.food2.append(li1)
            self.food2.append(",")
        elif(bt4 == True):
            self.food3.append(li1)
            self.food3.append(",")
        else:
            print("no")

myJson = {}

# tempRecipe = open("C:/Users/jinhalim/Desktop/recipe_bot/food/국물.txt","r")
# newRecipe = open("./test.txt","w")
k=0
for root, subdirs, files in os.walk('./food'):
    for file in files:
        with open("./food/"+file, 'r') as tempRecipe:
            k += 1
            s = str(k)
            newRecipe = open("./food/"+s+".txt", 'w')
            i = 0
            for line in tempRecipe.readlines():
                subline = line.split('\n')
                myJson[i] = subline[0]
                i += 1
            i = 0
            bt1 = False # 제목
            bt2 = False # 재료
            bt3 = False # 육수
            bt4 = False # 양념
            name_count = 0
            all_recipe = {}
            r = Recipe() 
            for i in range(len(myJson)):
                if(myJson[i] == "[제목]"):
                    n=0
                    # newRecipe.writelines( [%n for n in r.getall()])
                    for n in r.getall():
                        newRecipe.writelines(n)
                    newRecipe.writelines("\n")

                    print(r.getall())
                    r = Recipe() 
                    name_count += 1
                    bt1 = True
                    bt2 = False
                    bt3 = False
                    bt4 = False
                    # print(myJson[i])
                elif(myJson[i] == "[재료]"):
                    bt1 = False
                    bt2 = True
                    bt3 = False
                    bt4 = False
                    # print(myJson[i])
                elif(myJson[i] == "[육수]"):
                    bt1 = False
                    bt2 = False
                    bt3 = True
                    bt4 = False
                    # print(myJson[i])
                elif(myJson[i] == "[양념]"):
                    bt1 = False
                    bt2 = False
                    bt3 = False
                    bt4 = True
                    # print(myJson[i])
                else:
                    r.insert_list(myJson[i],bt1,bt2,bt3,bt4)
            newRecipe.close()
            tempRecipe.close()