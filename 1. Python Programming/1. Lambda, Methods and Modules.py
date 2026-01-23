#Lambda Function -> aka anonymous function
#Multiple arguments, but only one logic
sq=lambda x:x**2
print(f'Lambda function:{sq(4)}')
even=lambda x:x%2==0
#filter function 
#filter(function,iterable)
L=[1,2,3,4,5]
filterL=list(filter(even,L))
print(f'Even no.s list:{filterL}')

#MAP FUNCTION
#map(function,iterable)
mapL=list(map(sq,L))
print(f'Squared list:{mapL}')

#These three functions optimize the code

#MODULES -> math,random,os,datetime,time,pickle
#pickle is massively used in MachineLearning
#OS moduke can interact with the computer OS

#MATH Module
import math 
print(f'Ceiling value : {math.ceil(4.4)}') #round off to higher integer
print(f'Floor value : {math.floor(4.4)}') #round off to lower integer
print(f'Integer root of 27 : {math.isqrt(27)}')
print(f'2 power 8:{math.pow(2,8)}')

#RANDOM Module
import random
Cars=["Audi","Ferrari","Porshe","McLaren","Tesla","Lamborghini","Volswagen","Benz","Kogneiseigg"]
print(f'Cars list:{Cars}')
print(f'Random element from the cars list: {random.choice(Cars)}')
print(f'Random Integer : {random.randint(1,6)}') #includes 6 also
print(f'Random value b/w 0 and 1 : {random.random()}') #does not include 1.0
print(f'Random sample of size 3 from Cars : {(random.sample(Cars,3))}')
{random.shuffle(Cars)} #modifies the cars list itself
print(f'Random shuffle : {Cars}')
