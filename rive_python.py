#!/usr/bin/python3

# Python 3 example

from rivescript import RiveScript 
import re
rs = RiveScript(utf8=True)
# rs.set_handler("python", None)
rs.unicode_punctuation = re.compile(r'[.,!?;:]')
rs.load_directory("./rivescript")
rs.sort_replies()

print("""
Type /quit when you're done to exit this example.
""")
print("Bot> 무엇이 필요하신가요?")
print("1: 요리 검색\n2: 재료 검색\n3: 기타")
while True:
    msg = input("You> ")
    if msg == '/quit':
        quit()
    reply = rs.reply("localuser", msg)
    print("Bot>", reply)

