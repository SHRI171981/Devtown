# OOP -> Object Oriented Programming
print(f'OOP -> Object Oriented Programming\n')

'''SYNTAX of class:
class Name_of_the_class():
    statements'''

'''SYNTAX of object:
object_name=class_name(arguments)'''

class First():
    def pass_or_fail(self,marks):
        if marks>75:
            print("pass")
        else:
            print("fail")

object_name=First() #becoming an object of the class
object_name.pass_or_fail(90) #using the functionality

#SCOPE OF VARIABLES
var=10 #GLOBAL VARIABLE
def random_function(inp):
    var=8 #LOCAL VARIABLE
    print(inp+var)
random_function(12)

#INHERITANCE
class animal: #PARENT CLASS
    def speak(self):
        print("Animal is speaking")
class Dog(animal): #CHILD CLASS
    def bark(self):
        print("The dog barks")
    
obj=animal()
obj1=Dog()
obj.speak()
obj1.bark()
obj1.speak() #speak function usable in Dog also

#MULTI-LEVEL OOP
del animal,Dog
class animal: #PARENT CLASS
    def speak(self):
        print("Animal is speaking")
class Dog(animal): #CHILD CLASS
    def bark(self):
        print("The dog barks")
class Puppy(Dog):
    def eat(self):
        print("The puppy is eating")
    
obj2=Puppy()
obj2.eat()
obj2.bark() #Bark can be used in puppy
obj2.speak() #speak can be used in puppy












