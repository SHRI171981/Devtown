import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr1=arr1.reshape(2,5)
arr2=np.array([11,12,13,14,15,16,17,18,19,20])
arr2=arr2.reshape(2,5)

#Adding/Subtracting two matrices
print(f'arr1+arr2:\n{arr1+arr2}\n')

#Adding/Subtracting an element
print(f'Adding 20 to arr1:\n{arr1+20}\n')

arr3=([1,2,3,4,5])
print(f'arr1+arr3(According to rows)\n{arr1+arr3}\n')

#Division
print(f'arr1/arr2:\n{arr1/arr2}\n')

#Exponentiation
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr2=np.array([10,9,8,7,6,5,4,3,2,1])
arr1=arr1.reshape(2,5)
arr2=arr2.reshape(2,5)
print(f'arr1 to the power arr2:\n{arr1**arr2}\n')
print(f'arr1 sq:\n{arr1**2}\n') 

# MULTIPLICATION 
#   -> CROSS 
#   -> DOT 

#CROSS PRODUCT
print("MULTIPLICATION OF MATRICES\n\n")
print(f'Cross Product of arr1*arr2:\n{arr1*arr2}\n')

#DOT PRODUCT
arr2=arr2.reshape(5,2)
print(f'Dot product of arr1 and arr2(dot):\n{np.dot(arr1,arr2)}\n')
print(f'Dot product of arr2 and arr1(dot):\n{np.dot(arr2,arr1)}\n')

#                                   OR

print(f'Dot product of arr1 and arr2(matmul):\n{np.matmul(arr1,arr2)}\n')
print(f'Dot product of arr2 and arr1(matmul):\n{np.matmul(arr2,arr1)}\n')

#LINEAR ALGEBRA
# -> np.linalg : All linear algebra functions

#DETERMINANT
det_array1=np.array([[1,2],[3,4]])
print(f'2x2 MATRIX:\n{det_array1}\n')
print(f'Determinant:\n{np.linalg.det(det_array1)}\n')
det_array2=np.array([1,2,3,4,5,6,7,8,12])
det_array2=det_array2.reshape(3,3)
print(f'3x3 MATRIX:\n{det_array2}\n')
print(f'Determinant:\n{np.linalg.det(det_array2)}\n')

#TRANSPOSE
print(f'Transpose of 2x2:\n{det_array1.transpose()}\n')
print(f'Transpose of 3x3:\n{det_array2.transpose()}\n')


#INVERSE
print(f'Inverse of 2x2:\n{np.linalg.inv(det_array1)}\n')
print(f'Inverse of 3x3:\n{np.linalg.inv(det_array2)}\n')

#RECIPROCAL
arr=np.array([[10,20],[30,40.0]])
print(np.reciprocal(arr))

#STATISTICS
stat_arr=np.array([20,50,-40,9,10,-1,7,56,34])
stat_arr=stat_arr.reshape(3,3)
print(f'stat_arr:\n{stat_arr}\n')

#max/min
print(f'max:\t{np.max(stat_arr)}\n')
print(f'Max in each row:   {np.max(stat_arr,axis=1)}\n')
print(f'Min in each column:   {np.min(stat_arr,axis=0)}\n')

#sum
print(f'Sum of the array:    {np.sum(stat_arr)}\n')
print(f'Sum of each row:    {np.sum(stat_arr,axis=1)}\n')
print(f'Sum of each column:    {np.sum(stat_arr,axis=0)}\n')

#argmax -> Returns the index of the maximum element
print(f'max index no.:\t{np.argmax(stat_arr)}\n')
print(f'Max index in each row:   {np.argmax(stat_arr,axis=1)}\n')
print(f'Min index in each column:   {np.argmin(stat_arr,axis=0)}\n')

#around -> Round off to nearest integer... returns float value
arr=[0.55,0.96]
print(f'Rounded off array:\t{np.around(arr)}\n')
print(f'Rounded off to 1st decimal:\t{np.around(arr,decimals=1)}\n')

#floor and ceil

#COPY AND VIEW
arr=np.array([1,2,3,4])
arr_copy=arr.copy()
arr_view=arr.view()
arr[2]=5
print(f'Changes in arr does not affect the copy:\n\tarr:{arr}\tcopy:{arr_copy}\n')
print(f'Changes in arr does affect the view:\n\tarr:{arr}\tview:{arr_view}\n')

arr=np.array([1,2,3,4,5,6,7,8,9])
arr=arr.reshape(3,3)
print(arr)

print('Iterating over array:')
for i in np.nditer(arr):
    print(i)

print('Iterating over first row:')
for i in np.nditer(arr[0]):
    print(i)