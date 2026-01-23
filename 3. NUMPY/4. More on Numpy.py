import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[11,12,13],[14,15,16]])

#STACKING

#vstack -> Vertical Stack #No. of columns same
print(f'Vertical stack arr1-arr2:\n{np.vstack((arr1,arr2))}\n')
print(f'Vertical stack arr1-arr2-arr2-arr1:\n{np.vstack((arr1,arr2,arr2,arr1))}\n')

#hstack -> Horizontal Stack #No. of rows same
print(f'Horizontal stack arr1-arr2:\n{np.hstack((arr1,arr2))}\n')
print(f'Horizontal stack arr1-arr2-arr2-arr1:\n{np.hstack((arr1,arr2,arr2,arr1))}\n')

#dstack -> Depth Stack #No. of elements same
print(f'Depth stack arr1-arr2:\n{np.dstack((arr1,arr2))}\n')
print(f'Depth stack arr1-arr2-arr2-arr1:\n{np.dstack((arr1,arr2,arr2,arr1))}\n')
print(f'For 2 arrays:\n{np.dstack(([1,2,3,4],[5,6,7,8]))}')

#SPLITTING -> Breaking down into smaller arrays

arr=np.array([1,2,3])
print(f'Split array:\n{np.array_split(arr,3)}\n')
print(f'0th element:\n{np.array_split(arr,3)[0]}\n')
print(f'If 4 parts:\n{np.array_split(arr,4)}\n')
print(f'Unequal splitting:\n{np.array_split(arr,2)}\n')

#SEARCHING 

arr=np.array([1,2,3,4,5,4,4])
print(f'Indices of 4:\n{np.where(arr==4)}\n')
print(f'Indices of >=4:\n{np.where(arr>=4)}\n')


#SORTING

arr=np.array([12,4,21,-1,4,5.2,29,0])
print(f'Sorted array ASCENDING:\n{np.sort(arr)}\n')
print(f'Sorted array DESCENDING:\n{-np.sort(-arr)}\n') #use - 


# ANY() and ALL() methods
arr=np.array([2,4,6,8,9])
print(f'Any value satisfies even:\t{np.any(arr%2==0)}\n')
print(f'All values satisfy even:\t{np.all(arr%2==0)}\n')


#resize function -> same as reshape.... repeat the elements where there is shortage

arr=np.arange(12)
print(f'Resized 3x5 arr:\n{np.resize(arr,(3,5))}\n')
print(f'Resized 10x12 arr:\n{np.resize(arr,(10,12))}\n')


#delete -> Discard some elements
#delete(arr,obj,axis)

arr=np.array([1,2,3,4,3,5])
print(f'One dimension delete:\t{np.delete(arr,2)}') #deletes number at index 2
arr=arr.reshape(2,3)
print(f'Matrix:\n{arr}\n')
print(f'Two dimension delete:\t{np.delete(arr,3)}\n')
print(f'Two dimension delete from rows:\n{np.delete(arr,2,axis=1)}\n') #2nd column deleted
print(f'Two dimension delete from columns:\n{np.delete(arr,0,axis=0)}\n') #0th row deleted


#LCM -> Lowest Common Multiple
print(f'LCM of 25 and 125:\t{np.lcm(25,125)}\n')
print(f'LCM of 25,125 and 625:\t{np.lcm.reduce((25,125,625))}\n')
arr=np.array([2,4,6,8,10])
print(f'LCM of array:\t{np.lcm.reduce(arr)}\n')

#GCD -> Greatest Common Divisor
print(f'GCD of 6 and 27:\t{np.gcd(6,27)}\n')
print(f'GCD of 6,9 and 27:\t{np.gcd.reduce((6,9,27))}\n')
print(f'GCD of array:\t{np.gcd.reduce(arr)}\n')

#LINEAR EQUATION
#Consider 3x+y=9
#         x+2y=8
a=np.array([[3,1],[1,2]]) #coefficient matrix
b=np.array([9,8]) #solution matrix
print(f'Solution of linear eq:\t{np.linalg.solve(a,b)}\n')

#QUADRATIC EQUATION
#Consider x**2-5*x+6=0
coeff=np.array([1,-5,6])
print(f'Solution of quad eq:\t{np.roots(coeff)}\n')

#Vdot -> Vertical Dot Product
arr1=([[1,2,3],[4,5,6]])
arr2=([[10,20,30],[40,50,60]])
print(f'Vertical dot prod:\t{np.vdot(arr1,arr2)}\n')
# 1*10 + 2*20 + ... 6*60









  