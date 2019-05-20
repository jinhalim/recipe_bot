food_name = "미역"
have_food = False
import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root',password ='root',charset = 'utf8',db = 'recipe_db')
sql = "select * from recipe"
curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    food_ings = row['ingredient']
    if(food_ings.find(food_name) > 0):
        have_food = True
    if(have_food == True):
        print(row['ID'],":",row['recipe_name'])
        have_food = False
conn.close()