import shutil
import os
import numpy as np
from sklearn.model_selection import KFold

'''
this python is runnning after importnii.py. 
Shuffle 120 cases (.npy) to training folder and 30 cases to testing folder. should be mentioned that this is not cross-validation.
'''

t12_npy = r'D:\Python_scripts\sarcopenia-statistics\data\ppt12'
image_npy = r'D:\Python_scripts\sarcopenia-statistics\data\raw'
t4_npy = r'D:\Python_scripts\sarcopenia-statistics\data\ppt4'

images = os.listdir(image_npy)
t12s = os.listdir(t12_npy)
t4s = os.listdir(t4_npy)

ss = KFold(n_splits=5, shuffle=True)
arr_train = []
arr_test = []
for train_index, test_index in ss.split(images):
    print(test_index)
    arr_train.append(train_index)
    arr_test.append(test_index)

arr_train = np.array(arr_train)
arr_test = np.array(arr_test)

np.save(f'./save_npy/shuffle/train.npy', arr_train)
np.save(f'./save_npy/shuffle/test.npy', arr_test)

for f in range(5):
    for i in range(len(images)):
        npy = images[i].replace('.nii', '.npy').replace('.gz', '')
        if i in arr_train[f]:
            shutil.copy(fr'./save_npy/raw_t12/{npy}', fr'./save_npy/shuffle/{f}/train/raw_t12/{npy}')
            shutil.copy(fr'./save_npy/t12/{npy}', fr'./save_npy/shuffle/{f}/train/t12/{npy}')
            shutil.copy(fr'./save_npy/raw_t4/{npy}', fr'./save_npy/shuffle/{f}/train/raw_t4/{npy}')
            shutil.copy(fr'./save_npy/t4/{npy}', fr'./save_npy/shuffle/{f}/train/t4/{npy}')
            shutil.copy(fr'./save_npy/major/{npy}', fr'./save_npy/shuffle/{f}/train/major/{npy}')
            shutil.copy(fr'./save_npy/minor/{npy}', fr'./save_npy/shuffle/{f}/train/minor/{npy}')

        elif i in arr_test[f]:
            shutil.copy(fr'./save_npy/raw_t12/{npy}', fr'./save_npy/shuffle/{f}/test/raw_t12/{npy}')
            shutil.copy(fr'./save_npy/t12/{npy}', fr'./save_npy/shuffle/{f}/test/t12/{npy}')
            shutil.copy(fr'./save_npy/raw_t4/{npy}', fr'./save_npy/shuffle/{f}/test/raw_t4/{npy}')
            shutil.copy(fr'./save_npy/t4/{npy}', fr'./save_npy/shuffle/{f}/test/t4/{npy}')
            shutil.copy(fr'./save_npy/major/{npy}', fr'./save_npy/shuffle/{f}/test/major/{npy}')
            shutil.copy(fr'./save_npy/minor/{npy}', fr'./save_npy/shuffle/{f}/test/minor/{npy}')

        else:
            raise "check your folder, my dear"