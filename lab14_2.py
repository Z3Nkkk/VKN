import requests
from bs4 import BeautifulSoup 
import random

r=requests.get('https://unsplash.com/s/photos/programming')
soup= BeautifulSoup (r.text,'html.parser')    
images = []

if r.status_code==200:       
    for img in soup.findAll('img'):
        images.append(img.get('src'))

for i in range(4):
    el = random.randint(0, len(images)-1)
    image = requests.get(images[el])
    with open(str(i) + 'new_image.jpeg', 'wb') as f:
        f.write(image.content)
        f.close()