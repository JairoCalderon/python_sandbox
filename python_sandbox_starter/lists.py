# A List is a collection which is ordered and changeable. Allows duplicate members. = array

#Creating list
numbers = [1,2,3,4,50]
fruits = ["apples", "oranges", "grapes", "pears"]

#using a constructors
numbers2 = list((1,2,3,4,5))

#built-in functions

#gettig values
print(fruits[1])

#chaging a value
fruits[0]= "melon"

#getting the lenght of the array/list
print(len(fruits))

#adding (append) an item to the list
fruits.append("mangos")

print(fruits)

#remove from the list an specific element
fruits.remove("grapes")
print(fruits)

#insert to a specific position
fruits.insert(2, "watermelon")
print(fruits)

#remove from a specific position
fruits.pop(3)
print(fruits)

#reverse the list
fruits.reverse()

#sort list alphabetically
fruits.sort()

#sort list reverse alphabetically
fruits.sort(reverse=True)