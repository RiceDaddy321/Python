#tuples cannot be easily changes after creation
pi_tuple = (3, 1, 4, 1, 5, 9) #are made by surrounding the items with a paranthases
#they can be chaged by converting it to a list change it then convert it back

new_tuple = list(pi_tuple)
#make desired changes
new_list = tuple(new_tuple)

##len(new_tuple) max(new_tuple) min(tuple) 