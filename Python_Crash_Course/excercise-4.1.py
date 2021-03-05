# initialize and declare pizza list
favoritePizzas = ['Dominoes', 'Little Ceasers', 'Papa John\'s']

# loop through list
for pizza in favoritePizzas:
    print('I love pizza from ' + pizza)
# 4.11
friend_pizzas = favoritePizzas[:]
friend_pizzas.append('Pizza Hut')

print('My favorite pizzas are: ')
for pizza in favoritePizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
