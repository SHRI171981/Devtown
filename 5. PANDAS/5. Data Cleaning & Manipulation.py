import pandas as pd
import numpy as np

data1 = np.random.randn(10,3)
data2 = np.random.randn(7,3)
 
df1=pd.DataFrame(data1,columns=['col1','col2','col3'])
df2=pd.DataFrame(data2,columns=['col1','col2','col3'])
df=pd.concat([df1,df2],ignore_index=True)

print(' Elements of col3:')
for i in df['col3']:
    print(i)
print('\n')

print('Iterating over columns:\n')
for keys,values in df.items():
    print(keys,values)
print('\n')

print('Iterating over rows:\n')
for index,row in df.iterrows():
    print(index,row)
print('\n')

data=np.random.randn(10,3)
df=pd.DataFrame(data,columns=['col1','col2','col3'],index=[4,1,6,4,9,10,12,23,11,1])
print(f'Given df:\n{df}\n')

#SORT
print(f'Sorted on index:\n{df.sort_index()}')
print('Sorted on values:\n',df.sort_values(['col1']),'\n')
print('Sorted based on row index 9:\n',df.sort_values([9],axis=1),'\n')

df=pd.DataFrame(np.random.randn(5,3),index=['A','C','F','B','D'],columns=['Col1','Col2','Col3'])
#print('Given df:\n',df,'\n')                                                                                                                              

df=df.reindex(['A','B','C','D','E','F','G']) #if extra index is given, NaN values are stores
print(f'Reindexed df:\n{df}\n')

print(f'Checking Null values using isnull:\n{df.isnull()}\n')
print(f'Checking Null values using isna:\n{df.isna()}\n')
print(f'Checking non-Null values:\n{df.notnull()}\n')

print(f'Total no. of null values per column:\n{df.isnull().sum()}\n')
print(f'Total no. of null values in the df:\t{df.isnull().sum().sum()}\n')
print('Nan values in rowF:\n',df.loc['F'].isnull(),'\n')

print(f'Count of non-NaN values:\n{df.count()}\n')
print('Count of non-NaN values in col1:\t',df['Col1'].count(),'\n')

#fillna
print(f'Filling NaN values with Zeroes:\n{df.fillna(0)}\n')
print('Filling NaN values with Forward values:\n',df.ffill(),'\n')
print('Filling NaN values with backward values:\n',df.bfill(),'\n')

#dropna
print(f'Delete all Nan rows:\n{df.dropna()}\n')
print(f'Delete all Nan columns:\n{df.dropna(axis=1)}\n')

df = pd.DataFrame({'Apples':[34,132,87,81],'Mangoes':[53,13,53,66],'Bananas':[55,65,7,53]})
print(f'Df:\n{df}')
#print(f'53 replaced by 59:\n{df.replace({53:59})}\n')
#print('0th element of Apples replaced by 59:\n',df.replace({df['Apples'][0]:59}),'\n')

#Handling Duplicates
print('Duplicates in Mangoes column:\n',df.duplicated(subset=['Mangoes']),'\n')
print('Duplicates in Mangoes column removed:\n',df.drop_duplicates(subset=['Mangoes']),'\n')




#IMPORTING & EXPORTING a dataset

#IMPORT:
#SYNTAX:
# df=pd.read_'file_type'

#EXPORT:
#SYNTAX:
# df=pd.to_csv('')