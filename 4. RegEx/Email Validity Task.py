import re
inp=input("Enter an email:\t")
inp=inp.lower()
if len(inp)<=100:
    s1=re.split('@',inp)
    s2=re.split('\.',s1[1])
    s3=[]
    s3+=[s1[0]]+[s2[0]]+[s2[1]]
    valid1=re.search('\w+',s3[0])
    valid2=re.search('[a-z]',s3[1])
    valid3=re.search('[a-z]',s3[2])  
    if valid1 and (valid2 and len(s3[1])<=10) and (valid3 and len(s3[2])<=3):
        print("VALID")
    else:
        print("INVALID")
else:
    print("INVALID")