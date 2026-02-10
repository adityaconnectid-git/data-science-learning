## Topic: Operations and properties

## Properties

## For the type
import numpy as np
arr = np.array([1,3,5,54,1,6])
print(arr.dtype)
print(arr)

## For typecasting in array
int_arr = arr.astype(float)
print(int_arr)
print(int_arr.dtype)

## For the shape
ones_array = np.ones((2,3))
print(ones_array.shape)
print(ones_array)

## For the size
print(ones_array.size)

## For the dimention
arr_1 = np.array([[1,2],[2,3],[4,5],[6,7]])
print(arr_1.ndim)
print(arr_1)

## Operations
arr_2 = np.array([3,4,1,5])
print(arr_2)
print(arr_2 + 2)
print(arr_2 / 2)
print(arr_2 ** 2)
print(arr_2 // 2)
print(arr_2 % 2)
print(np.square(arr_2))

## Aggregation function
arr_3 = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr_3)
print(np.sum(arr_3))
print(np.mean(arr_3)) 
print(np.min(arr_3))
print(np.max(arr_3))
print(np.std(arr_3)) 
print(np.var(arr_3))

# Zeros + Ones
# Ek 3×4 ka array banao jisme:
# pehli row = zeros
# baaki rows = ones

zeros_row = np.zeros((1, 4)) 
ones_rows = np.ones((2, 4))  
final_array = np.vstack((zeros_row, ones_rows))
print(final_array)

# Ek 1D array banao:
# [1,2,3,4,5,6]
# Use reshape karke 2×3 bana do.

arr_ = np.array([1, 2, 3, 4, 5, 6])
print("Original 1D Array:", arr_)
reshaped_arr = arr_.reshape(2, 3)
print("\nReshaped 2x3 Array:")
print(reshaped_arr)

# Filter the value 
arr_4 = np.array([5, 12, 7, 20, 3, 18])
print(arr_4)
filtered = arr_4[arr_4 > 10]
print(filtered)

# Compare Two Arrays
# Do arrays banao:
# a = [1, 2, 3]
# b = [4, 5, 6]
# indication do kya a + b valid hai NumPy me
# result print karo

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)