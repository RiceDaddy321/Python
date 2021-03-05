# A list of items that cannot change (immutable)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# looping through a tuple
for dimension in dimensions:
    print(dimension)

# altough you cannot modify a tuple you can assign a new value to a variable that is one
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
