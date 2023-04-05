# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name= 'Brad'
age= 37

#Concatinate

# print('hello, my name is ' + name + 'and I am ' + age) This will give an erro pq contatinating integers will not work
# print('hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

#arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-strings (python 3.6+)
# print(f'Hello my name is {name} and I am {age}')

# String Methods
s= 'hello world'

#capitalize
print(s.capitalize())

