# -*- coding: utf-8 -*-
import codecs
import re
import pandas
from config import *

#считаем стоп-слова
ffile = codecs.open('stopwords.txt', 'r', encoding='utf8')
try:
    stops = ffile.read()
finally:
    ffile.close()

# читаем файл
ffile = codecs.open('messages_' + FRIEND_ID + '.txt', 'r', encoding='utf8')
try:
    txt = ffile.read()
finally:
    ffile.close()

# выбираем слова через регулярные выражения
res = re.findall(ur'[А-Яа-я]+', txt, re.U)
stopwords = re.findall(ur'[А-Яа-я]+', stops, re.U)

print 'Насобирали повторяющихся слов', len(res)
res = [x.lower() for x in res]
print 'Выкинем оттуда короткие слова (считай - буквы)'
res = [x for x in res if x not in stopwords and len(x) > 1]

words = pandas.Series(res)
print words.value_counts()[:WORDS_COUNT]