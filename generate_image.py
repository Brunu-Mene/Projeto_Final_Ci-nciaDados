from PIL import Image
from tqdm import tqdm
import numpy as np
import os
def imagetensor(imagedir):
  for i, im in tqdm(enumerate(os.listdir(imagedir))):
    try:
        image= Image.open(imagedir + '/' + im)
    except:
        continue
    image= image.convert('HSV')
    if i == 0:
      images= np.expand_dims(np.array(image, dtype= float)/255, axis= 0)
    else:
      image= np.expand_dims(np.array(image, dtype= float)/255, axis= 0)
      try:
        images= np.append(images, image, axis= 0)
      except:
        continue
  return images

X_train_0 = imagetensor('train/0/')
X_train_1 = imagetensor('train/1/')
X_test_0 = imagetensor('test/0/')
X_test_1 = imagetensor('test/1/')
X_train = np.append(X_train_0, X_train_1, axis= 0)
X_test = np.append(X_test_0, X_test_1, axis= 0)
y_train = np.append(np.zeros(X_train_0.shape[0]), np.ones(X_train_1.shape[0]))
y_test = np.append(np.zeros(X_test_0.shape[0]), np.ones(X_test_1.shape[0]))

#save the data
import pickle
pickle.dump(X_train, open('X_train_g.pkl','wb'))
pickle.dump(y_train, open('y_train_g.pkl','wb'))
pickle.dump(X_test, open('X_test_g.pkl','wb'))
pickle.dump(y_test, open('y_test_g.pkl','wb'))
