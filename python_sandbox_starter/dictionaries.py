# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#similar to obejct literal in JavaScript

#creatign a dictionary
person = {
    'firstName' : 'John',
    'lastName' : "Doe",
    'age' : 30
}


#using a constructor
# person2 = dict(firstName='Sara', lastName='Williams')


# print(person2, type(person2))

#getting a value
print(person['firstName'])
print(person.get('lastName'))

#add key/value
person['phone'] = '6478524152'

#getting dict keys
print(person.keys())

#getting dict items
print(person.items())