#Numpy -> A python library
# Numerical Python
import numpy as np
import time

'''
a=np.random.rand(500000000) #values between 0 and 1 100000000 times

#list
start=time.time()
mean_list=sum(a)/len(a)
print('Using List:',time.time()-start)

#numpy
start=time.time()
mean_np=np.mean(a)
print('Using Numpy:',time.time()-start)
'''

#SYNTAX for numpy array
# arr = np.array() #initialization

# 0 Dimensional
arr = np.array(4) #single value
print(f'0 Dimesional array: {arr}')

# 1 Dimensional
arr1 = np.array([1,2,3,4,5]) # a list of values
print(f'1 Dimensional array: {arr1}')

# 2 Dimensional 
arr2 = np.array([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,1]]) # Matrix of values
print(f'2 Dimensional array: {arr2}')

# 3 Dimensional
arr3 = np.array([[[1,2,3,4],[5,6,7,8]],[[8,7,6,5],[4,3,2,1]]])
print(f'3 Dimensional array: {arr3}')
print(f'type of arr3: {type(arr3)}')

#CHECKING dimension 
print(f'Dimension of arr3: {arr3.ndim}')

# n-dim array
arrn = np.array([1,2,3,4,5],ndmin=10)
print(f'ndim array: {arrn}') #creates a 10-dimensional array

arrn2 = np.array([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,1]],ndmin=10)
print(f'10 dimensional array: {arrn2}')

#SHAPE ATTRIBUTE -> Tells about the size of array (i.e rows and columns)
print(f'Shape of arr3: {arr3.shape}')
# answer -> (2,2,4)
# Here, there are 2 2D arrays, 2 1D arrays(list) inside each 2D array and 4 0D arrays(ele) inside each 1D array

#dtype -> data-type
print(f'Datatype of array: {arrn.dtype}')
arr3=np.array(['Mango','Orange','Apple'])
print(f'Type of arr3: {arr3.dtype} where U -> Unicode')

arr4=np.array(['Mango','Orange','Apple',65,3,4.3])
print(f'Type of arr4: {arr4.dtype}')

print('-> Numpy array accepts all datatypes')

#CHANGING TYPE
arr5=np.array([1,2,3,4],dtype='S')
print(f'Type of arr5: {arr5.dtype}')

#Size -> Total no. of elements in an array
print(f'Size of arr3: {arr3.size}')
print(f'Size of row in arr2: {np.size(arr2,1)}')
print(f'Size of column in arr2: {np.size(arr2,0)}')

#Itemsize -> Shows storage occupied
print(f'Storage occupied by each element in arr2: {arr2.itemsize} bytes')
print(f'Total size occupied by arr2: {arr2.nbytes} bytes')
