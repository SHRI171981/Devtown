import pandas as pd

# 1. DATA EXPLORATION

student = {'Name':['Rahul','Rohit','Venkat','Sahil','Ankita'],
           'OS':[75,75,96,10.5,100],
           'DBMS':[20,80,60,40.0,99]}
stud=pd.DataFrame(student)
robin={'Name':'Robin','OS':62.5,'DBMS':56}
stud=stud._append(robin,ignore_index=True) #ignore_index is compulsary
vishnu={'Name':'Vishnu','OS':66,'DBMS':99}
vishnu=pd.DataFrame(vishnu,index=[0])
stud=pd.concat([stud,vishnu],ignore_index=True) #ignore_index avoids duplication
print(f'Given df:\n{stud}\n')


print('First 3 samples:\n',stud.head(3),'\n')
print('Last 3 samples:\n',stud.tail(3),'\n')
print(f'Datatypes:\n{stud.dtypes}\n')
print(f'is_empty of stud:\t{stud.empty}\n')
print(f'Dimension of stud:\t{stud.ndim}\n')
print(f'Shape of stud:\t{stud.shape}\n')
print(f'Size of stud:\t{stud.size}\n')
print(f'values of stud:\n{stud.values}\n')
print(f'Columns names of stud:\n{stud.keys}\n')

print(f'Describe the df:\n{stud.describe()}\n')

print(f'Transpose of stud:\n{stud.T}\n')
print(f'Sum of colunms:\n{stud.sum()}\n')
print('Sum of OS and DBMS column:\n',stud[['OS','DBMS']].sum(),'\n')
print(f'Row-Wise sum:\n',stud[['OS','DBMS']].sum(1),'\n')
print('Mean of OS and DBMS column:\n',stud[['OS','DBMS']].mean(),'\n')
print('Row-Wise Mean:\n',stud[['OS','DBMS']].mean(1),'\n')
print('Median of OS and DBMS column:\n',stud[['OS','DBMS']].median(),'\n')
print('Row-Wise Median:\n',stud[['OS','DBMS']].median(1),'\n')
print('Mode of OS and DBMS column:\n',stud[['OS','DBMS']].mode(),'\n')
print('SD of OS and DBMS column:\n',stud[['OS','DBMS']].mean(),'\n')
print('Row-Wise SD:\n',stud[['OS','DBMS']].mean(1),'\n')
print('Min of OS and DBMS column:\n',stud[['OS','DBMS']].min(),'\n')
print('Row-Wise Max:\n',stud[['OS','DBMS']].max(1),'\n')
