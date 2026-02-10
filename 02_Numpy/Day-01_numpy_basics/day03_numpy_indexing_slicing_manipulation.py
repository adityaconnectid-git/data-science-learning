## Day: 3 - Numpy
## Topic: Indexing , slicing , Reshaping , Manipulation and Array Modification

## Indexing
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[0])
print(arr[4])
print(arr[-1])

## Slicing
print(arr[1:5])
print(arr[:4])
print(arr[::2])
print(arr[::-1]) # It is reverse the array

## Fancy indexing
print(arr[[0, 2, 4]]) # It print only those value which are given

## Filtering Data
print(arr[arr>25])

## Reshaping
## 1d to nd
reshapes_arr = arr.reshape(2, 3) # reshape usually returns a view if possible, otherwise a copy
print(reshapes_arr)
print(arr)

## nd to 1d
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.ravel()) # returns a view if possible
print(arr_2d.flatten()) # always returns a copy

## Array Modigication
## Insert in 1D
print(arr)
new_arr = np.insert(arr, 2, 100)
print(new_arr)

## Insert in 2D
# insert a new row at index 1
print(arr_2d)
new_arr_2d = np.insert(arr_2d, 1, [5,6,7], axis=0)
print(new_arr_2d)
# insert a new coloum at index 2
print(arr_2d)
new_arr_2d_col = np.insert(arr_2d, 2, [7, 8], axis=1)
print(new_arr_2d_col)
# for the single line 
new_arr_2d_sig = np.insert(arr_2d, 2, [7, 8], axis=None)
print(new_arr_2d_sig)

## Use the append
print(arr)
new_app_arr = np.append(arr , [4, 5, 6])
print(new_app_arr)

## Concatenate
"""
np.concatenate((array1, array2), axis=0)
axis 0 > vertical stacking
axis 1 > horizontal stacking
"""
arr1 = np.array([1,2,3])
arr2 = np.array([5,6,7])
new_arr1 = np.concatenate((arr1, arr2))
print(new_arr1)
# for row or vertical
new_arr2 = np.concatenate((arr1, arr2), axis=0)
print(new_arr2)

## Removing a element
# from 1d
print(arr)
new_del_arr = np.delete(arr, 0)
print(new_del_arr)
# from 2d
print(arr_2d)
new_del_2d_arr = np.delete(arr_2d, 0, axis=0)
print(new_del_2d_arr)

## Stacking
print(arr1)
print(arr2)

print(np.vstack((arr1, arr2))) # vertically stack
print(np.hstack((arr1, arr2))) # horizontal stack

## split
# split equaly
print(arr)
print(np.split(arr, 2))
# horizontal 
print(np.hsplit(arr, 2))
# vertical
print(arr_2d)
print(np.vsplit(arr_2d, 2))