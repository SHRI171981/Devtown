#DataFrame (D and F capital)
# 2-Dimensional

import pandas as pd
#Syntax
#pd.DataFrame(data,index,columns,dtype,copy)

#CREATING A DATAFRAME
#   -> List   -> Dict   -> ndarrays    -> Series(Combining)    -> Using another DF

df=pd.DataFrame()
print(f'Empty df:\n{df}\n')

#Creating using list
data=[7,8,44,56,23,98]
df=pd.DataFrame(data)
print(f'Creating using list:\n{df}\n')

data=[['Dog','Bhaw Bhaw'],['Cat','Meow'],['Cow','Moo']]
df=pd.DataFrame(data)
print(f'Using list of lists:\n{df}\n')
#changing column name:
df=pd.DataFrame(data,columns=['Animal Name','Animal Sound'])
print(f'Column names changed:\n{df}\n')

#Creating using dict
data={'Name':['Ram','Rahul','Ramesh'],'Age':[25,32,42]}
df=pd.DataFrame(data)
print(f'Creating using dict:\n{df}\n')

#CREATING USING SERIS
data={"Karan_Marks":pd.Series([50,77,65]),'Arjun_Marks':[45,32,89]}
df=pd.DataFrame(data)
print(f'Creating using series:\n{df}\n')

data={'a':pd.Series([1,2,3],index=['x','y','z']),'b':pd.Series([4,5,6,7],index=['x','y','z','w'])}
df=pd.DataFrame(data)
print(f'Unequal indices:\n{df}\n')

data={'a':pd.Series([1,2,3],index=['x','y','z']),'b':pd.Series([4,5,6,7],index=['x','y','z','w'])}
df=pd.DataFrame(data,columns=['p','q'])
print(f'Changing Column Names:\n{df}\n')

#CREATING USING A LIST OF DICTIONARIES
data=[{'A':1,'B':2},{'C':3,'D':4},{'E':5,'F':6}]
df=pd.DataFrame(data)
print(f'Creating using dictionaries:\n{df}\n')

#UPDATING A DaTAFRAME
#Selecting a particular column
data=[10,20,30,40,50,60,70]
dataa=[70,60,50,40,30,20,10]
df=pd.DataFrame([data,dataa],columns=['A','B','C','D','E','F','G'])
print(f'Given Dataframe:\n{df}\n')
print(f'Selecting particular column:\n{df["C"]}\n')

#Adding a column
df['H']=[80,80]
print(f'Df with new column:\n{df}\n')

#Using series
df['I']=pd.Series([90,90,40])
print(f'Using series:\n{df}\n') #it left out the value 40

df['J']=pd.Series([56])
print(f'Nan values:\n{df}\n')

df['K']=pd.Series([10,20,30,40],index=[0,1,2,3])
print(f'Extra indices:\n{df}\n')

df['L']=pd.Series([10,20,30,40],index=[7,8,9,10])
print(f'Diff indices:\n{df}\n')

#DELETING A COLUMN
data=[10,20,30,40,50,60,70]
dataa=[70,60,50,40,30,20,10]
df=pd.DataFrame([data,dataa],columns=['A','B','C','D','E','F','G'])
print(f'Given Dataframe:\n{df}\n')

#USING del KEYWORD
del df['B'] #cannot be used for multiple deletion
print(f'df with B column deleted:\n{df}\n')

#USING pop function
df.pop('C')
print(f'df with C column deleted:\n{df}\n')

#USING drop function
print(f'df with F and G column deleted at once:\n{df.drop(["F","G"],axis=1)}\n')

#Adding columns:
df['J']=df['A']+df['E']
print(f'Columns A and E added as J:\n{df}\n')

data=[10,20,30,40,50,60,70]
dataa=[70,60,50,40,30,20,10]
df=pd.DataFrame([data,dataa],columns=['A','B','C','D','E','F','G'])
df1=[{'A':45,'B':98,'C':76,'D':88}]
df=df._append(df1)
print(f'Appended df:\n{df}\n')
df1=pd.DataFrame([data])
df1=df1.insert(2,'B',10)
print(df1)

