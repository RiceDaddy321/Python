# if else elif
'''
== equal to
!= not equal to
> greater than
>= greater than or equal to
< less than
<= less than or equal to
'''

age = 30

if age > 16:
    print('You are old enough to drive')
else:
    print("You are not old enough to drive")

if age >= 21:
    print("You are old enough to drive a tractor or trailer")
elif age >= 16:
    print("You are old enough to drive a car")
else:
    print("You are not old enough to drive")

# logical operators: and or not

if ((age >= 1) and (age <= 18)): #once one of these conditions are met: the program wont go through any of the others
    print("you get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif not(age == 30):
    print("you don't get a birthday")
else:
    print("Yay, you get a birthday!")
