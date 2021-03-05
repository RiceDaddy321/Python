# initialize an empty list
motorcycles = []

# using the append method to create a dynamic list
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')

print(motorcycles)

# del keyword can remove elements from a list
del motorcycles[0]

print(motorcycles)

# Using the pop method, you both remove the item
# and can still use the value of the removed element
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.append('Harley-Davidson')
motorcycles.append('Ford')
motorcycles.append('Ducati')

first_owned = motorcycles.pop(0)
print('first owned motorcycle is a ' + first_owned)

# If the value is known then use the remove method
motorcycles.remove('Harley-Davidson')
print(motorcycles)

# you can use range(lower bound(inclusive), upper bound(exclusive)) to generate numbers
for value in range(1, 6):
    print(value)

# Statistics with Lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehension - generate a list using a single line
squares = [value**2 for value in range(1, 11)]
print(squares)
# To make a comprehension list you need to name the list something discriptive
# open a set of square brackets and define the expression for the values you want to
# store in the list. Then write a for loop to generate the numbers you want to feed
# into the expression

# Slicing a list to use part of the whole rather than a single (or whole) element
print(squares[0:3])
#[first element(incluseive):final element(exclusive)] omitting either bound means the upper

# copying a list
my_foods = ['Pizza', 'Falafel', 'Carrot Cake']
friend_foods = my_foods[:]
#using: friend_foods = my_foods, would make them point to the same list, thus making them equal

my_foods.append('Cannoli')
friend_foods.append('Ice cream')

print("My favorite foods are: ")
print(my_foods)

print("My friend's favorite foods are: ")
print(friend_foods)
