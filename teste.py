#train test split
import pandas as pd
from PIL import Image
from tqdm import tqdm
import urllib.request
import os
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

for i in tqdm(range(0, len(avatares))):
    url = avatares.values[i]
    try: 
       
        
        with urllib.request.urlopen(url) as url:
            image = Image.open(url)
            images.append(image.resize((64,64)))
            images[i].save('images/'+str(i)+'.jpg')
        
            
          
    except:
        indexes_to_drop.append(i)
    continue

#save indexes_to_drop to drop from data_ml into images folder 
import pickle
pickle.dump(indexes_to_drop, open('images/indexes_to_drop.pkl','wb'))