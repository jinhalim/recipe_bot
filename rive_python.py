#!/usr/bin/python3

# Python 3 example

from rivescript import RiveScript
import re
rs = RiveScript(utf8=True)
rs.unicode_punctuation = re.compile(r'[.,!?;:]')
rs.load_directory("./rivescript")
rs.sort_replies()

print("""This is a bare minimal example for how to write your own RiveScript bot!

For a more full-fledged example, try running: `python rivescript brain`
This will run the built-in Interactive Mode of the RiveScript library. It has
some more advanced features like supporting JSON for communication with the
bot. See `python rivescript --help` for more info.

example3.py is just a simple script that loads the RiveScript documents from
the 'brain/' folder, and lets you chat with the bot.

Type /quit when you're done to exit this example.
""")
print("Bot> 무엇이 필요하신가요?")
while True:
    msg = input("You> ")
    if msg == '/quit':
        quit()
    reply = rs.reply("localuser", msg)
    print("Bot>", reply)

# vim:expandtab


# 출처: https://dlwodus.tistory.com/339?category=972785 [MY MEMO]