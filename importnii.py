''' The code is implemented on python 3.8.12. Please note that

for i in range(45):
    nii1 = sitk.ReadImage(os.path.join(t12_dir, t12s[i]))
    arr1 = sitk.GetArrayFromImage(nii1)

    vector = np.sum(np.sum(arr1, axis=1), axis=1)
    t12_seg_level = np.argwhere(vector == np.max(vector))[0][0]

    caseid = t12s[i].replace('.nii.gz', '').replace('pp', '')
    slice2d = arr1[t12_seg_level, :, :]

    if slice2d.shape[0] != 512 or slice2d.shape[1] != 512:
        print(f'{images[i]} should be resized')
        slice2d = A.resize(slice2d, 512, 512, interpolation=cv2.INTER_CUBIC)

    slice2d[slice2d < 0.5] = 0.
    slice2d[slice2d >= 0.5] = 1.

    vector_1 = np.sum(np.sum(arr1, axis=0), axis=1)
    if np.sum(vector_1[0:255]) > np.sum(vector_1[256:512]):
        print(f'{images[i]} will rotate 180 degrees')
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/t12/{caseid}.npy', slice2d)

    nii2 = sitk.ReadImage(os.path.join(image_dir, images[i]))
    arr2 = sitk.GetArrayFromImage(nii2)

    assert np.shape(arr1) == np.shape(arr2)

    caseid = images[i].replace('.gz', '').replace('.nii', '')
    slice2d = arr2[t12_seg_level, :, :]

    slice2d[slice2d < -29.] = -529.
    slice2d[slice2d > 150.] = 650.

    if np.sum(vector_1[0:255]) > np.sum(vector_1[256:512]):
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/raw_t12/{caseid}.npy', slice2d)

'''

import SimpleITK as sitk
import os
import albumentations as A
import numpy as np
import cv2

t12_dir = r'D:\Python_scripts\sarcopenia-statistics\data\ppt12'
image_dir = r'D:\Python_scripts\sarcopenia-statistics\data\raw'
t4_dir = r'D:\Python_scripts\sarcopenia-statistics\data\ppt4'

images = os.listdir(image_dir)
t12s = os.listdir(t12_dir)
t4s = os.listdir(t4_dir)
'''
for i in range(100):
    nii1 = sitk.ReadImage(os.path.join(t12_dir, t12s[i]))
    arr1 = sitk.GetArrayFromImage(nii1)

    vector_1 = np.sum(np.sum(arr1, axis=1), axis=1)
    t12_seg_level = np.argwhere(vector_1 == np.max(vector_1))[0][0]

    caseid = t12s[i].replace('.nii.gz', '').replace('pp', '')
    slice2d = arr1[t12_seg_level, :, :]

    if slice2d.shape[0] != 512 or slice2d.shape[1] != 512:
        print(f'{caseid} will be resized')
        slice2d = A.resize(slice2d, 512, 512, interpolation=cv2.INTER_CUBIC)
        slice2d[slice2d < 0.5] = 0.
        slice2d[slice2d >= 0.5] = 1.

    vector_2 = np.sum(np.sum(arr1, axis=0), axis=1)
    if np.sum(vector_2[0:255]) > np.sum(vector_2[256:512]):
        print(f'{caseid} will rotate 180 degrees')
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/t12/{caseid}.npy', slice2d)

    nii2 = sitk.ReadImage(os.path.join(image_dir, images[i]))
    arr2 = sitk.GetArrayFromImage(nii2)

    assert np.shape(arr1) == np.shape(arr2)

    caseid = images[i].replace('.gz', '').replace('.nii', '')
    slice2d = arr2[t12_seg_level, :, :]

    if slice2d.shape[0] != 512 or slice2d.shape[1] != 512:
        slice2d = A.resize(slice2d, 512, 512, interpolation=cv2.INTER_CUBIC)

    slice2d[slice2d < -29.] = -500.
    slice2d[slice2d > 150.] = 500.

    if np.sum(vector_2[0:255]) > np.sum(vector_2[256:512]):
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/raw_t12/{caseid}.npy', slice2d)

'''
'''

for i in range(100):
    nii1 = sitk.ReadImage(os.path.join(t4_dir, t4s[i]))
    arr1 = sitk.GetArrayFromImage(nii1)

    vector_1 = np.sum(np.sum(arr1, axis=1), axis=1)
    t4_seg_level = np.argwhere(vector_1 == np.max(vector_1))[0][0]

    caseid = t12s[i].replace('.nii.gz', '').replace('pp', '')
    slice2d = arr1[t4_seg_level, :, :]

    slice2d[slice2d == 2.] = 1.

    if slice2d.shape[0] != 512 or slice2d.shape[1] != 512:
        print(f'{caseid} will be resized')
        slice2d = A.resize(slice2d, 512, 512, interpolation=cv2.INTER_CUBIC)
        slice2d[slice2d < 0.5] = 0.
        slice2d[slice2d >= 0.5] = 1.

    vector_2 = np.sum(np.sum(arr1, axis=0), axis=1)
    if np.sum(vector_2[0:255]) > np.sum(vector_2[256:512]):
        print(f'{caseid} will rotate 180 degrees')
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/t4/{caseid}.npy', slice2d)

    nii2 = sitk.ReadImage(os.path.join(image_dir, images[i]))
    arr2 = sitk.GetArrayFromImage(nii2)

    assert np.shape(arr1) == np.shape(arr2)

    caseid = images[i].replace('.gz', '').replace('.nii', '')
    slice2d = arr2[t4_seg_level, :, :]

    if slice2d.shape[0] != 512 or slice2d.shape[1] != 512:
        slice2d = A.resize(slice2d, 512, 512, interpolation=cv2.INTER_CUBIC)


    slice2d[slice2d < -29.] = -500.
    slice2d[slice2d > 150.] = 500.

    if np.sum(vector_2[0:255]) > np.sum(vector_2[256:512]):
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/raw_t4/{caseid}.npy', slice2d)


'''
for i in range(80):
    nii1 = sitk.ReadImage(os.path.join(t4_dir, t4s[i]))
    arr1 = sitk.GetArrayFromImage(nii1)

    vector_1 = np.sum(np.sum(arr1, axis=1), axis=1)
    t4_seg_level = np.argwhere(vector_1 == np.max(vector_1))[0][0]

    caseid = t12s[i].replace('.nii.gz', '').replace('pp', '')
    slice2d = arr1[t4_seg_level, :, :]

    slice2d[slice2d == 2.] = 0.

    if slice2d.shape[0] != 512 or slice2d.shape[1] != 512:
        print(f'{caseid} will be resized')
        slice2d = A.resize(slice2d, 512, 512, interpolation=cv2.INTER_CUBIC)
        slice2d[slice2d < 0.5] = 0.
        slice2d[slice2d >= 0.5] = 1.

    vector_2 = np.sum(np.sum(arr1, axis=0), axis=1)
    if np.sum(vector_2[0:255]) > np.sum(vector_2[256:512]):
        print(f'{caseid} will rotate 180 degrees')
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/major/{caseid}.npy', slice2d)

for i in range(80):
    nii1 = sitk.ReadImage(os.path.join(t4_dir, t4s[i]))
    arr1 = sitk.GetArrayFromImage(nii1)

    vector_1 = np.sum(np.sum(arr1, axis=1), axis=1)
    t4_seg_level = np.argwhere(vector_1 == np.max(vector_1))[0][0]

    caseid = t12s[i].replace('.nii.gz', '').replace('pp', '')
    slice2d = arr1[t4_seg_level, :, :]

    slice2d[slice2d == 1.] = 0.
    slice2d[slice2d == 2.] = 1.

    if slice2d.shape[0] != 512 or slice2d.shape[1] != 512:
        print(f'{caseid} will be resized')
        slice2d = A.resize(slice2d, 512, 512, interpolation=cv2.INTER_CUBIC)
        slice2d[slice2d < 0.5] = 0.
        slice2d[slice2d >= 0.5] = 1.

    vector_2 = np.sum(np.sum(arr1, axis=0), axis=1)
    if np.sum(vector_2[0:255]) > np.sum(vector_2[256:512]):
        print(f'{caseid} will rotate 180 degrees')
        slice2d = slice2d[::-1]

    np.save(f'./save_npy/minor/{caseid}.npy', slice2d)









