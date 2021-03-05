# 4.3
for value in range(1, 21):
    print(value)
# 4.4
oneMillion = [value * 1 for value in range(1, 1000001)]
# for value in oneMillion:
#   print(value)
# 4.5
print(min(oneMillion))
print(max(oneMillion))
print(sum(oneMillion))
# 4.6
oddNumbers = []
for value in range(1, 20, 2):
    oddNumbers.append(value)
    print(value)
# 4.7
threeMultiples = [value * 3 for value in range(1, 11)]
print(threeMultiples)
# 4.8-9
cubes = [value**3 for value in range(1, 11)]
print(cubes)
# 4.10
print("The first three cubes are: ")
for cube in cubes[:4]:
    print(cube)

print("Three items from the middle of the list are: ")
lowerbound = len(cubes) / 2 - 1
upperbound = len(cubes) / 2 + 2

for cube in cubes[int(lowerbound):int(upperbound)]:
    print(cube)

print("Last three items in list: ")
upperbound = len(cubes) - 3
for cube in cubes[int(upperbound):]:
    print(cube)
