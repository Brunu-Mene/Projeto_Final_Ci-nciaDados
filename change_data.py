#copy folders train and test to new folers that will be reduced by 5000 images only

import os
import shutil
import random
import numpy as np
import pandas as pd
from tqdm import tqdm
#creating folders
if not os.path.exists('train_reduced'):
    os.makedirs('train_reduced')
if not os.path.exists(('train_reduced/0')):
    os.makedirs('train_reduced/0')
if not os.path.exists(('train_reduced/1')):
    os.makedirs('train_reduced/1')
if not os.path.exists('test_reduced'):
    os.makedirs('test_reduced')
if not os.path.exists(('test_reduced/0')):
    os.makedirs('test_reduced/0')
if not os.path.exists(('test_reduced/1')):
    os.makedirs('test_reduced/1')



#copying 5000 images from train and test folders to new folders
for i in tqdm(range(5000)):

    #read a random image file name 
    e = random.choice(os.listdir('train/0'))    
    
    shutil.copy('train/0/'+'{}'.format(e), 'train_reduced/0/'+'{}'.format(e))
    e = random.choice(os.listdir('train/1'))    
    
    shutil.copy('train/1/'+'{}'.format(e), 'train_reduced/1/'+'{}'.format(e))
    
for i in  tqdm(range(2500)):

    e = random.choice(os.listdir('test/0'))
    shutil.copy('test/0/'+'{}'.format(e), 'test_reduced/0/'+'{}'.format(e))
    e = random.choice(os.listdir('test/1'))

    shutil.copy('test/1/'+'{}'.format(e), 'test_reduced/1/'+'{}'.format(e))

