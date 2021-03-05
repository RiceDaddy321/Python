# store destinations in a list
travelDestinations = ['Germany', 'France', 'England', 'Russia', 'Spain']

# print the array
print(travelDestinations)

# use sorted() to print the list alphabetically(temp)
print(sorted(travelDestinations))

# prove that the og list was not altered
print(travelDestinations)

# Use reverse() to change the order of the list(permenant)
travelDestinations.reverse()
print(travelDestinations)

# reverse the change to the list
travelDestinations.reverse()
print(travelDestinations)

# Use sort to change the list so it's stored in alphabetical order.
travelDestinations.sort()
print(travelDestinations)

# Use sort to change the list in reverse alphabetical order.
travelDestinations.sort(reverse=True)
print(travelDestinations)
