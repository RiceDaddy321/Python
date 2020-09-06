for x in range(0, 10):  # start at 0 and work up to 10 but not include it
    print(x, " ", end="")

print("\n")

grocery_list = ['juice', 'tomatoes', 'bananas',
                'apples']

for y in grocery_list:  # cycle through list
    print(y)

for x in [2, 4, 6, 8, 10]:  # specifies what to store in x
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
