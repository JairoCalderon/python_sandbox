# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


#creating a function
def sayHello(name):
    print(f'Hello {name}')

sayHello('John Doe')

#we can also set a default value for the as argument
def sayHello2(name = 'Sam'):
    print(f'Hello {name}')

sayHello2()

#return values
def getSum (num1, nume2):
    total = num1 + nume2
    return total

receipt = getSum(3,5)
print(receipt)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
#similar to arow functions

getSum2 = lambda num1, num2 : num1 + num2

print(getSum2(5,6))
