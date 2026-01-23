import numpy as np

#CREATE 
print("CREATE:-\n")
arr=np.array([[1,2,3],[4,5,6]])
print(arr.ndim)

#zero array -> initialisation
arr=np.zeros((3,3)) # n elements gives a 2dim array
print(f'Two dimensional array:\n {arr}\n')

arr10=np.zeros(10)
print(f'Gives one dimensional array: {arr10}\n')

arrn=np.zeros((10,10))
print(f'10x10 matrix: \n {arrn}\n')

#ones array -> all values are 1
arr1=np.ones([3,3])
print(f'ones matrix size 3x3:\n {arr1}\n')

#empty array -> random values
arr_em=np.empty([4,4])
print(f'Random values array:\n {arr_em}\n')

#full array -> array filled with a particular value
arr_full=np.full([4,4],4)
print(f'Array with all 4s:\n {arr_full}\n')

#np.eye -> identity matrix
arr_iden=np.eye(3) #only one parameter is enough
print(f'Identity matrix of order 3:\n {arr_iden}\n')

#np.diag -> diagonal matrix
arr_diag=np.diag([1,2,3,4,5,6,7])
print(f'Diagonal matrix:\n {arr_diag}\n')

#np.linspace -> equally distributed values between the given limits
arr_lin=np.linspace(0,100,11)
print(f'Evenly distributed linspace elements:\n {arr_lin}\n')

#random values -> random values between 0&1
arr_rand=np.random.random(10)
print(f'Random value array between 0 and 1:\n {arr_rand}\n')

arr_randint=np.random.randint(15,25,size=(2,3))
print(f'Random values array between 15 and 25:\n {arr_randint}\n') 

#arange function -> take values in a given range
arr_ar=np.arange(1,15,2)
print(f'Arange array from 1-15 is:\n {arr_ar}\n')

del arr,arr1,arr10,arr_ar,arrn,arr_diag,arr_em,arr_full,arr_iden,arr_lin,arr_rand,arr_randint


#UPDATION
print("UPDATE:-\n")
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr3=np.array([
                [
                    [1,2,3],
                    [4,5,6]
                ],
                [
                    [7,8,9],
                    [10,11,12]
                ]
                ])
#Indexing
print(f'Accessing 1D array:\t{arr1[2]}')
print(f'Accessing 2D array:\t{arr2[1,2]}')
print(f'Accessing 3D array:\t {arr3[0,1,1]}\n')

#Updating value:
arr3[1,1,2]=-1
print(f'Updated arr3:\n{arr3}\n')

#Slicing -> arr[i:j,k:l,m:n] and so on
print(f'Sliced arr2:\n{arr2[1:]}\n')
print(f'Sliced 2D array of arr3:\n{arr3[0:1]}\n')
print(f'Sliced 1D array from arr3:\n{arr3[0,1,0:2]}\n')

#Reshape 
arr_2mat=np.arange(0,60,5)
arr_2mat=arr_2mat.reshape(3,4)
print(f'Reshaped 3x4 matrix:\n{arr_2mat}\n')

arr_3mat=np.arange(0,60,5)
arr_3mat=arr_3mat.reshape(3,2,2)
print(f'Reshaped 3D matrix:\n{arr_3mat}\n')

arr_rmat=np.random.randint(1,100,63)
arr_rmat=arr_rmat.reshape(7,9)
print(f'Random elements matrix:\n{arr_rmat}\n')

del arr1,arr2

#Appending an array to an existing array
arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr2=np.array([[13,14,15,16]])
arr2=np.append(arr1,arr2,axis=0)
print(f'Appended array:\n{arr2}\n')

#Adding two array ('+') -> Add respective entries
arr1=np.array([[1,2,3,4],[5,6,7,8]])
arr2=np.array([[9,10,11,12],[13,14,15,16]])
print(f'arr1+arr2=\n{arr1+arr2}\n')

#Scalar addition/subtraction
print(f'Scalar 10 added to arr1:\n{arr1+10}\n')

#Scalar multiplication/division
print(f'Scalar multiplication of arr1 by 10:\n{arr1*10}\n')

#Scalar exponentiation
print(f"arr1 squared:\n{arr1**2}\n")

#Array Multiplication -> Each element multiplied by corresponding elements
print(f'Multiplication of arr1 and arr2:\n{arr1*arr2}\n')
