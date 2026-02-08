## Topic: Numpy basics

## Creating array using list in python
import numpy as np
arr = np.array([1,3,5,54,1,6])
print(arr.shape)
print(arr.dtype)
print(arr)

## With defualt value of 0
zeroes_array = np.zeros(3)
print(zeroes_array.shape)
print(zeroes_array.dtype)
print(zeroes_array)

## With defualt value of 1
ones_array = np.ones((2,3))
print(ones_array.shape)
print(ones_array.dtype)
print(ones_array)

## Value according you 
filled_array = np.full((2,3), 7)
print(filled_array.shape)
print(filled_array.dtype)
print(filled_array)

## Creating sequence of numbers in numpy
arr_1 = np.arange(1,10,2)
print(arr_1.shape)
print(arr_1.dtype)
print(arr_1)

## Creating identity matrix
identity_matrix = np.eye(3)
print(identity_matrix.shape)
print(identity_matrix.dtype)
print(identity_matrix)