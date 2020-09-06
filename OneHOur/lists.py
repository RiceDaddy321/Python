import random
import sys
import os

grocery_list = ['juice', 'tomatoes', 'bananas',
                'apples']

print('first item: %s' % (grocery_list[0]))

grocery_list[0] = 'Green Juice'
print('first item: %s' % (grocery_list[0]))

print(grocery_list[1:3])  # prints from index 1 to 3 not including 3

other_events = ['Wash car', 'Pick up kids', 'Cash check']

to_do_list = [other_events, grocery_list]  # lists can store other lists
print(to_do_list)

print(to_do_list[1][1])

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, "Pickles")
print(grocery_list)
grocery_list.remove("Pickles")
print(grocery_list)

grocery_list.sort()
print(grocery_list)

grocery_list.reverse()
print(grocery_list)

del grocery_list[4]
print(grocery_list)

to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))
