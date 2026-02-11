## Day: 04 - Numpy
## Topic: Broadcasting & Vectorization, Handling missing values

# Broadcasting
import numpy as np

prices = np.array([100, 200, 300])
discount = 10 # scalar single value
final_price = prices - (prices * discount/100)
print(final_price)

arr_marks = np.array([65, 34, 78])
result = arr_marks * 2
print(result)

matrix = np.array([[1, 2, 3], [5, 6, 7]])
vector = np.array([10, 20, 30])
sum_of_two_matrix = matrix + vector
print(sum_of_two_matrix)

# error condition
# Broadcasting requires compatible shapes.
# Reshaping is one workaround, but should be used carefully.
arr1 = np.array([[1, 2, 3], [5, 6, 7]]) # shape [2,3]
arr2 = np.array([1,3]) # shape [1,2]
# sum_arr = arr1 + arr2
# print(sum_arr)
# solution
arr3 = arr1.reshape(3,2)
sum_arr_final = arr3 + arr2
print(arr3)
print(sum_arr_final)

## Vectorization
# Python loop is slower for large data
# NumPy vectorized operations are faster and preferred in Data Science
# Vectorise using list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# result_list = [x+y for x,y in zip(list1, list2)]
# print(result_list) 

result_list = []
for x, y in zip(list1, list2):
    result_list.append(x + y)
print(result_list)

## Fast vectorise approach
arr4 = np.array([2,3,5])
arr5 = np.array([8,9,3])
result_arr = arr4 + arr5
print(result_arr)

multiple = arr5 * 3
print(multiple)

## Handling missing values
arr6 = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr6))

# no, it is not a comparable
print(np.nan == np.nan)

# Replacing missing value
cleaned_arr = np.nan_to_num(arr6) # it is filed by default zero
print(cleaned_arr)
clean_arr = np.nan_to_num(arr6, nan=10)
print(clean_arr) # it is fill by given value

# present infinite  number in array
arr7 = np.array([1,2,np.inf,4,-np.inf,8])
print(np.isinf(arr7))
# replacing by finite number
cleaned_arr1 = np.nan_to_num(arr7, posinf=100, neginf=-100)
print(cleaned_arr1)