

import glob
import numpy as np
import SimpleITK as sitk
import pandas as pd
import os

t4_dir = './data/t4/*'
t12_dir = './data/t12/*'
l3_dir = './data/l3/*'

df = pd.DataFrame([0.,0.,0.,0.],index=['t12','major','minor','l3'],columns=['id'])

for f in glob.glob(t4_dir):
    print(f)
    nii = sitk.ReadImage(f)
    print(nii.GetSize())
    arr = sitk.GetArrayFromImage(nii)
    major, minor = np.sum(arr == 1), np.sum(arr == 2)
    print(major)
    print(minor)
    print(30*'=')
    df[os.path.basename(f).replace('_t4.nii.gz','')] = [0.,float(major),float(minor),0.]
'''
for f in glob.glob(t12_dir):
    nii = sitk.ReadImage(f)
    arr = sitk.GetArrayFromImage(nii)
    t12 = np.sum(arr == 1)
    df.loc[['t12'],os.path.basename(f).replace('_t12.nii.gz','')] = [float(t12)]

for f in glob.glob(l3_dir):
    nii = sitk.ReadImage(f)
    arr = sitk.GetArrayFromImage(nii)
    l3 = np.sum(arr == 1)
    df.loc[['l3'],os.path.basename(f).replace('_seg_L3.nii.gz','')] = [float(l3)]

del df['id']

print(df)

df.to_csv('./output/muscle_area.csv')

'''
