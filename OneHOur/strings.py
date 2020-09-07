long_string = "i'll catch those hands bruh"

print(long_string[0:4])

print(long_string[-5:])  # prints out the last four characters

print(long_string[:-5])  # prints everything up to the last 5 five letters of the string

print(long_string[:4] + "be there")

print("%c is my %s and my number %d number is %.5f" %
      ('X', 'favorite', 1, 3.14159))  # the string

print(long_string.capitalize())

print(long_string.find("Floor"))  # CASE SENSISTIVE, returns -1 if DNE

print(long_string.isalpha())  # checks if alphabetical

print(long_string.isalnum())  # checks if alphanumerical

print(len(long_string))

print(long_string.replace("hands", "toes"))

print(long_string.strip())  # removes trailing and leading whitespace

quote_list = long_string.split(" ")
print(quote_list)
