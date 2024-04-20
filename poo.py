# class et objet

from abc import ABC, abstractmethod


class Being(ABC):
    @abstractmethod
    def walk ():
        pass
        

class Person(Being):
    def __init__(self,name,age):
        print(type(age))
        Person.isageint(age)
        self.name = name
        self.age = age
        

    def walk(self):
        print("Im walking")

    @staticmethod
    def isageint(age):
        if type(age) == int:
            return True
        else:
            raise ValueError ("Value is not a int")

        


class Animal: 

    __age = 10

    def __init__(self) :
        self.name = "Animal"

    def talk(self): 
        pass

    def __str__(self):
        return self.name

#heritage
class Dog(Animal):  
   
    def talk(self): #polymorphism
        print(f"I'm {self.name}")

    

my_dog = Dog()

my_dog.talk()

print(my_dog)
print(my_dog._Animal__age) # acceder à un atribut privé

you = Person("Alex", 20)
you.walk()
