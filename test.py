import pymysql

result = ""
recipe = "오뎅탕"
recipe_id = 0
conn = pymysql.connect(host = 'localhost',user = 'root',password ='root',charset = 'utf8',db = 'recipe_db')
sql = "select * from big_category where category_name = %s"
curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute(sql,recipe)
rows = curs.fetchall()
for row in rows:
    recipe_id = row['id']
newsql = "select * from recipe where sub_id = %s"
curs.execute(newsql,recipe_id)
rows = curs.fetchall()
for row in rows:
    result = result + str(row['ID']) + ":" + row['recipe_name']+"\n"
print(result)
conn.close()