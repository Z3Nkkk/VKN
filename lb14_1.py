from bs4 import BeautifulSoup
import requests 
import json

print("Введіть ключові слова")
words = input()
words = words.split(" ")

urls = open('urls.txt', 'r')
urls_reader = urls.read()
urls_reader = urls_reader.split("\n")
count_dict = {}

count = 0


for word in words:
    count = 0
    for el in urls_reader:
        r = requests.get(el)
        if r.status_code==200:
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            text = text.replace("\n", ' ')
            text = text.split(' ')
            for i in text:
                if word == i:
                    count += 1
            count_dict[word] = count        

with open("count_words.json", "x", encoding = 'utf8') as jsonfile:
    data = json.dumps(count_dict,  ensure_ascii = False, indent = 4)
    jsonfile.write(data)
