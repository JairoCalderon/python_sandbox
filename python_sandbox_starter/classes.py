# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#creating classes
class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def birthday(self):
        self.age += 1


#extend class
class Customer(User):
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def setBalance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balnce}'

#intialize user object
brad = User("Brad Traversy", "bradtrav@email.com", 30)

#initialize a costumer
jenny = Customer("Janet Johnson", "jane@traversy.com", 45)

jenny.setBalance(500)

brad.birthday()

print(brad.greeting())

