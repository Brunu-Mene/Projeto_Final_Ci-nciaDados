#train test split
import pandas as pd
from PIL import Image
from tqdm import tqdm
import urllib.request
import os

import requests
from PIL import Image
import shutil
import urllib


if not os.path.exists('images'):
    os.makedirs('images')
else:
    #delete all files in images folder
    for file in os.listdir('images'):
        os.remove(os.path.join('images', file))

feData = pd.read_csv('data/ifood-restaurants-february-2021.csv')
avatares = feData['avatar']

images = [] 

indexes_to_drop = []

sleep_time = 0

for i in tqdm(range(50000, len(avatares))):
    url = avatares.values[i]
    
    response = requests.get(url)
    if response.status_code:
        try:
            fp = open(f'images/{str(i)}.jpg', 'wb')
            fp.write(response.content)
            fp.close()

            image = Image.open(f'images/{str(i)}.jpg')
            image.thumbnail((64,64))
            image.save(f'images/{str(i)}.jpg')
        except:
            indexes_to_drop.append(i)
    else:
        indexes_to_drop.append(i)

print(indexes_to_drop)