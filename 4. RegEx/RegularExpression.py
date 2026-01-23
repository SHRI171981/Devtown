#DATA CLEANING
# -> Very useful for using Pandas
import re


#FINDALL

stri="I was occupied on Sunday, and after I got free, I called my friend whose number was 111-9876543210" #find phone number from this

number=re.findall('\d',stri)
print(f'\tDigits in stri:\n{number}\n')

number=re.findall('\d+',stri)
print(f'Numbers in string:\n{number}\n')

number=re.findall('\d{3}-\d{10}',stri)
print(f'Pattern of number:\n{number}\n')

stri2="I was occupied on Sunday, and after I got free, I called my friend whose number was 111-9876543210 and 109-5793485389"

number=re.findall('\d+-\d+',stri2) #works with  \d+ also
print(f'All such numbers in stri2:\n{number}\n')


#SEARCH
stri3='On this day' 
if re.search('^On',stri3):
    print("MATCHED")
else:
    print("UNMATCHED")


#MATCH
stri='Dog is a pet animal'
mat=re.match('D\w\w',stri)
print(f'String starting with D: {mat.group()}')


#SPLIT 
stri='On Monday, there is a high chance of rainfall'
spli1=re.split("\s",stri) #works with jus ' ' also
spli2=re.split('\s',stri,2) #first 2 split, rest as it is
print(f'Separate words:\n{spli1}\n')
print(f'2 Splits:\n{spli2}\n')


#SUB -> Replace
stri='feetball is net a spert ef feet' # have to replace e with o
rep=re.sub('e','o',stri)
print(f'Replaced string:\n{rep}\n')


# -> Methods :
#     1. \d -> DIGIT
#     2. \w -> WORD/CHAR (A-Z,a-z,0-9,_)
#     3. \s -> SPACE



# META CHARACTERS -> Making a character

# 1. [a-b] -> Set of characters
stri='Delhi is the capital of India'
asd=re.findall('[a-k]',stri)
print(f'All characters between a and k:\n{asd}\n')

#2. ^ -> Starts with
#3. $ -> Ends with
asd1=re.findall('^India',stri)
asd2=re.findall('India$',stri)
print(f'Starting with India:\t{asd1}\n')
print(f'Ending with India:\t{asd2}\n')


# '.' '*' '+' 
asd3='Delhi is inside india & inside the globe'
print(f'String:\n{re.split(" ",asd3)}\n')
asd4=re.findall('in*',asd3)
asd5=re.findall('in+',asd3)
asd6=re.findall('in.',asd3)
print(f'in* -> occurence:    {asd4}\n')
print(f'in+ -> occurence:    {asd5}\n')
print(f'in. -> occurence:    {asd6}\n')
