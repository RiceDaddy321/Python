message = 'Hello World'
multilineMessage = """This is a multi-line
example...bruh"""

print(message)
'''
#print(message[0:5]) - starts at the first index
and stops at, but does not include, the last index

#message.count('(character or string)') - counts the amonunt of occurcences of the string/character

#message.find('(character/string)') - looks for the first occurence of the given expression
#IMPORTANT--if it doesn't find it then it outputs a -1

#message.replace('(string to be replaced)', '(what to replace with)')
#IMPORTANT--it doesn't actually alter the original string, instead it returns the new string
#EASY FIX: message = message.replace(arg1, arg2)

#formatted string:
message = '{(placeholder for the greeting)}, {}. Welcome!'.format(placeholder1, placeHolder2)
alternative-> message = f'{placeHolder1}, {placeHolder2}. Welcoem!' --f string

#dir(variable)
shows all of the attributes and methods that we have access to

#help(variable type.())describes
'''


print(multilineMessage)
