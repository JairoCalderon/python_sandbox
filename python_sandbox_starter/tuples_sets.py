# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#creatign a tuple
fruits = ("apples", "oranges", "grapes")

#singles values needs trailing comma
fruits2 = ("oranges",)

#getting a value from a tupe
print(fruits[1])

#em Tuples can not change values, they are unschangechable
#fruits[0]= "watermelon" this won't work



# A Set is a collection which is unordered and unindexed. No duplicate members.

#creatign a set
fruitsSet={"apples","oranges", "mangos"}

#check if in the set
print("apples" in fruitsSet)

#adding to the set
fruitsSet.add("grapes")

#removing from the set
fruitsSet.remove("mangos")

#adding duplicate velues it won't work. It won't give an error, it'll just not add the extra duplicated value
fruitsSet.add("apples")

#clearing the set
# fruitsSet.clear()

#deleting a set
# del fruitsSet
