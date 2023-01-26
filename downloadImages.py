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

feData = pd.read_csv('data/ifood-restaurants-february-2021.csv')
noData = pd.read_csv('data/ifood-restaurants-november-2020.csv')
data = feData[feData['url'].isin(noData['url'])]

#removendo restaurantes com rating == 0 e == 5
data = data[(data['rating'] != 0)&(data['rating'] != 5)]
data = data.reset_index(drop=True)

avatares = data['avatar']


data['isElite'] = data['rating'].apply(lambda x: 1 if x >= 4.5 else 0)


# images = [] 

# indexes_to_drop = []

# sleep_time = 0

# for i in tqdm(range(130000, len(avatares))):
#     url = avatares.values[i]
#     try: 
#         response = requests.get(url)
#     except:
#         indexes_to_drop.append(i)
#         continue
#     if response.status_code:
#         try:
#             fp = open(f'images/{str(i)}.jpg', 'wb')
#             fp.write(response.content)
#             fp.close()

#             image = Image.open(f'images/{str(i)}.jpg')
#             image.thumbnail((64,64))
#             image.save(f'images/{str(i)}.jpg')
#         except:
#             indexes_to_drop.append(i)
#     else:
#         indexes_to_drop.append(i)

# print(indexes_to_drop)

#from the folder images, separate the images in folders of train and test, 75% train and 25% test
import os
import shutil
import random

#creating folders
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists(('train/0')): 
    os.makedirs('train/0')
if not os.path.exists(('train/1')):
    os.makedirs('train/1')
if not os.path.exists('test'):
    os.makedirs('test')
if not os.path.exists(('test/0')):
    os.makedirs('test/0')
if not os.path.exists(('test/1')):
    os.makedirs('test/1')


for i in tqdm(data.index): 
    if not os.path.isfile('images/'+'{}.jpg'.format(i)):
        continue
    if data['isElite'].values[i] == 1:
        if random.random() < 0.75:
            shutil.copy('images/'+ '{}.jpg'.format(i), 'train/1/'+'{}.jpg'.format(i))
        else:
            shutil.copy('images/'+ '{}.jpg'.format(i), 'test/1/'+'{}.jpg'.format(i))
    else:
        if random.random() < 0.75: 
            shutil.copy('images/'+ '{}.jpg'.format(i), 'train/0/'+'{}.jpg'.format(i))
        else:
            shutil.copy('images/'+ '{}.jpg'.format(i), 'test/0/'+'{}.jpg'.format(i))






        

# #sepating images in train and test folders
# for i in tqdm(data.index):
#     #check if image exists 
#     if not os.path.isfile('images/'+'{}.jpg'.format(i)):
#         continue
#     if random.random() < 0.75:
#         shutil.copy('images/'+ '{}.jpg'.format(i), 'train/'+'{}.jpg'.format(i))
#     else:
#         shutil.copy('images/'+ '{}.jpg'.format(i), 'test/'+'{}.jpg'.format(i))

