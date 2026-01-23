import pandas as pd
import numpy as np

#SERIES -> 1D array like
#SYNTAX:
#   pd.Series(data,index,dtype)

#Creating an empty series:
s=pd.Series()
print(f'Empty series:\t{s}')

#Creating series using Numpy array

data=np.array([12,45,32,89])
s=pd.Series(data)
print(f'Using numpy array:\n{s}\n')

s=pd.Series(data,index=[12,13,14,15])
print(f'Changed Index:\n{s}\n')

#Creating series using dictionary
data={'a':10,'b':40,'c':90,'d':95}
s=pd.Series(data)
print(f'Using dictionary:\n{s}\n')

s=pd.Series(data,index=['e','f','g','h'])
print(f'NaN index:\n{s}\n')

s=pd.Series(data,index=['c','d','e','b','a'])
print(f'Using dictionary:\n{s}\n')

#Creating series using scalar values
data=99
s=pd.Series(data,index=[101,102,103,104])
print(f'Using scalar value 99:\n{s}\n')


#Updating Series

#Accesing a particular element
data=np.array([12,54,32,13,-10,21,-0.5,0,15,7,-7])
s=pd.Series(data)
print(f'3rd element:\t{s[2]}\n')
print(f'First 3 elements:\n{s[:3]}\n')

#BOOLEAN MASKING
data={'a':10,'b':40,'c':90,'d':95,'e':15}
s=pd.Series(data)
print(f'Greater than 50 check:\n{s>50}\n')
print(f'Values greater than 50:\n{s[s>50]}\n')
print(s[['a','b']])

#print('Dropping index a:\n',s.drop('a'),'\n')
s.drop('a')
print(f"Temp delete 'a':\n{s}\n")

s.drop('a',inplace=True)
print(f"Permanent delete 'a':\n{s}")

