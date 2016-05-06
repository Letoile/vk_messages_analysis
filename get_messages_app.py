# -*- coding: utf-8 -*-
import vk
import codecs
import time
from config import *

session = vk.Session(access_token=TOKEN)
api = vk.API(session)

#get messages
start = 0
messages = api.messages.getHistory(uid=MY_ID, user_id=FRIEND_ID, start_message_id=start, rev=1)
print "Всего сообщений ", messages[0]
count = messages[0]
while count > 0:
        print "Осталось обработать сообщений ", count
        time.sleep(4)
        messages_list = api.messages.getHistory(uid=MY_ID, user_id=FRIEND_ID, offset=start, rev=1, count=200)
        count -= 200
        start += 201
        for text in messages_list[1:]:
            body = text['body']
            with codecs.open("messages_" + FRIEND_ID + ".txt", "a", "utf-8") as text_file:
                text_file.write(body + "\n")