import random
# used for when you have no idea how many times you're going to be looping

random_number = random.randrange(0, 100)

while(random_number != 15):
    print(random_number)
    random_number = random.randrange(0, 100)

i = 0

while (i <= 20):
    if(i % 2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1  # shorthand for i = i + 1 (works for all of the other operations)
        continue
    i += 1
