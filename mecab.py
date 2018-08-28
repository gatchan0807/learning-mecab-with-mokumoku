import re
import bs4
import sys
import MeCab
import urllib.request
from pprint import pprint

if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    print("URL指定がありません！")
    exit()

soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

title = soup.title.string
description = soup.find(attrs={
    "name": re.compile(r'Description', re.I)
}).attrs['content']
h1 = soup.h1.string
contents = title + description + h1
output_words = []

m = MeCab.Tagger()
keywords = m.parse(contents)

for row in keywords.split("\n"):
    word = row.split("\t")[0]
    if word == "EOS":
        break
    else:
        pos = row.split("\t")[1].split(",")[0]
        if pos == "品詞":
            output_words.append(word)

pprint(list(set(output_words)))
