import pandas as pd

data={'APPLES':[102,150,120,80],'GRAPES':[50,120,80,38]}
df=pd.DataFrame(data)
print(f'Given df:\n{df}\n')
print('Column grapes:\n',df[['GRAPES']],'\n')
df['BANANAS']=df['GRAPES']+20
print(f'Updated df:\n{df}\n')
df.drop(['BANANAS'],axis=1,inplace=True)
print(f'Permanent delete using drop:\n{df}\n')

data={'APPLES':[102,150,120,80],'GRAPES':[50,120,80,38]}
df=pd.DataFrame(data,index=['Delhi','Mumbai','Kolkata','Bengaluru'])
df['BANANAS']=df['GRAPES']+20
df['MANGOES']=df['GRAPES']+50
df['STRAWBERRIES']=df['APPLES']+21
df['ORANGES']=df['GRAPES']+43

#loc function
print('\t\tMumbai:\n',df.loc[['Mumbai']],'\n')
print('\t\tIndex 3:\n',df.iloc[[1]],'\n')
print('\t\tDelhi-Kolkata:\n',df.loc['Delhi':'Kolkata'],'\n')
print('\t\tIndex 1-3:\n',df.iloc[1:3],'\n')

#Append function to add a row
student = {'Name':['Rahul','Rohit','Venkat','Sahil','Ankita'],
           'OS':[25,75,96,10.5,100],
           'DBMS':[20,80,60,40.0,99]}
stud=pd.DataFrame(student)
print(f'\tData:\n{stud}\n')
robin={'Name':'Robin','OS':62.5,'DBMS':56}
stud=stud._append(robin,ignore_index=True) #ignore_index is compulsary
print(f'Adding row using _append:\n{stud}\n')

#Concat method to add a row
vishnu={'Name':'Vishnu','OS':66,'DBMS':99}
vishnu=pd.DataFrame(vishnu,index=[0])
stud=pd.concat([stud,vishnu],ignore_index=True) #ignore_index avoids duplication
print(f'Adding row using concat:\n{stud}\n')

#UPDATION
stud.loc[4]=['Ankit',29,99]
print(f'Updated stud:\n{stud}')

#DELETION
stud.drop(3,inplace=True)
print(f'Deleted row 3:\n{stud}\n')