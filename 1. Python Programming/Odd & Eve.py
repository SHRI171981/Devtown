#GAME NAME -> ODD/EVE

import random
L=["Bat","Ball"]
Ch=input("Enter Odd or Eve\t")
print("\n")
print(f'You chose {Ch}\n')
UserCh=int(input("Enter a number between 1&6\t"))
CompCh=random.randint(1,6)
print(f'User -> {UserCh} \t Comp -> {CompCh}')
toss=UserCh+CompCh
flag=""
if toss%2==0:
    if Ch=="Even":
        flag="User"
        print("You won the Toss!!!\n")
        UserChoice=input("User choose Bat/Ball\t")
        print(f'You chose to {UserChoice}\n')
    else:
        print("You lost the Toss\n")
        flag="Comp"
        CompChoice=random.choice(L)
        print(f'Computer chose to {CompChoice}\n')
else:
    if Ch=="Odd":
        flag="User"
        print("You won the Toss!!!\n")
        UserChoice=input("User choose Bat/Ball\t")
        print(f'You chose to {UserChoice}\n')
    else:
        print("You lost the Toss\n")
        flag="Comp"
        CompChoice=random.choice(L)
        print(f'Computer chose to {CompChoice}\n')
flag2=''
if flag=="User":
    if UserChoice=="Bat":
        print("User Batting\n")
        flag2="User"
    else:
        print("Comp Batting\n")
        flag2="Comp"
else:
    if CompChoice=="Bat":
        print("Comp Batting\n")
        flag2="Comp"
    else:
        print("User Batting\n")
        flag2="User"

CompScore=0
UserScore=0

print("Game Start\n")

if flag2=="User":
    print("User Batting : \n")
    UserInput=int(input())
    CompInput=random.randint(1,6)
    print(f'User -> {UserInput} \t Comp -> {CompInput}')
    while UserInput!=CompInput:
        UserScore+=UserInput
        UserInput=int(input())
        CompInput=random.randint(1,6)
        print(f'User -> {UserInput} \t Comp -> {CompInput}')
    print("OUT!!!")
    print(f'Score -> {UserScore}\n')
    print("Computer Batting : \n")
    UserInput=int(input())
    CompInput=random.randint(1,6)
    print(f'User -> {UserInput} \t Comp -> {CompInput}')
    while UserInput!=CompInput:
        CompScore+=CompInput
        UserInput=int(input())
        CompInput=random.randint(1,6)
        print(f'User -> {UserInput} \t Comp -> {CompInput}')
    print("OUT!!!")
    print(f'Score -> {CompScore}')

else:
    print("Computer Batting : \n")
    UserInput=int(input())
    CompInput=random.randint(1,6)
    print(f'User -> {UserInput} \t Comp -> {CompInput}')
    while UserInput!=CompInput:
        CompScore+=CompInput
        UserInput=int(input())
        CompInput=random.randint(1,6)
        print(f'User -> {UserInput} \t Comp -> {CompInput}')
    print("OUT!!!")
    print(f'Score -> {CompScore}\n')
    print("User Batting : \n")
    UserInput=int(input())
    CompInput=random.randint(1,6)
    print(f'User -> {UserInput} \t Comp -> {CompInput}')
    while UserInput!=CompInput:
        UserScore+=UserInput
        UserInput=int(input())
        CompInput=random.randint(1,6)
        print(f'User -> {UserInput} \t Comp -> {CompInput}')
    print("OUT!!!")
    print(f'Score -> {UserScore}')

if UserScore>CompScore:
    print("YOU WON")
elif UserScore<CompScore:
    print("YOU LOST")
else:
    print("MATCH DRAWN")