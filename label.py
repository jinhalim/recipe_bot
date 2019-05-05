import json

myJson = {}

tempRecipe = open("C:/Users/jinhalim/Desktop/recipe_bot/please_recipe_text/국물.txt","r")
newRecipe = open("./test.txt","w")

i = 0
for line in tempRecipe.readlines():
    subline = line.split('\n')
    myJson[i] = subline[0]
    i += 1

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
        
        
# newRecipe.writelines(r)

# r.print_all()
newRecipe.close()
tempRecipe.close()


