from PIL import Image
from tqdm import tqdm
import numpy as np
import os

import pandas as pd

data_ml = pd.read_csv('data_ml.csv')

X_tabular_train = []

X_tabular_test = []
y_tabular_train = []
y_tabular_test = []


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def imagetensor(imagedir, X_tabular,y_tabular):
  images = []
  for i, im in tqdm(enumerate(os.listdir(imagedir))):
    try:
        print()
        image= Image.open(imagedir + '/' + im)
        image= image.convert('HSV')
        X_tabular.append(data_ml.loc[int(j.split('.')[0])].drop(['isElite']))

    except:
        print("deu ruim")
        continue
    if i == 0:
      images= np.expand_dims(np.array(image, dtype= float)/255, axis= 0)
    else:
      image= np.expand_dims(np.array(image, dtype= float)/255, axis= 0)
      try:
        images= np.append(images, image, axis= 0)
      except:
        continue
  return images, X_tabular, y_tabular

X_train_0,X_tabular_train,y_tabular_train = imagetensor('train/0/',X_tabular_train, y_tabular_train)
X_train_1,X_tabular_train,y_tabular_train = imagetensor('train/1/',X_tabular_train,y_tabular_train)
X_test_0,X_tabular_test,y_tabular_test = imagetensor('test/0/',X_tabular_test,y_tabular_test)
X_test_1,X_tabular_test,y_tabular_test = imagetensor('test/1/',X_tabular_test,y_tabular_test)
print(X_train_0) 
print(X_train_1)

X_train = np.concatenate((X_train_0, X_train_1), axis=0)
X_test = np.concatenate((X_test_0, X_test_1), axis=0)


#save the data
import pickle
pickle.dump(X_train, open('X_train_g.pkl','wb'))
pickle.dump(X_test, open('X_test_g.pkl','wb'))

pickle.dump(X_tabular_train, open('X_tabular_train_g.pkl','wb'))
pickle.dump(y_tabular_train, open('y_tabular_train_g.pkl','wb'))
pickle.dump(X_tabular_test, open('X_tabular_test_g.pkl','wb'))
pickle.dump(y_tabular_test, open('y_tabular_test_g.pkl','wb'))

