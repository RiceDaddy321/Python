#! /usr/bin/python

from random import choice

def includes(text, *response):
    for index in range(len(response)):
        if text == response[index]:
            return True
            break

length = input("How many characters: ")
hasSpecialChar = input("Include Special characters(/*-,./()*&^%$#@!?<>|}{(|)):\"'")
hasNumbers = input("Has numbers: ")

hasSpecialChar = includes(hasSpecialChar, "y", "Y", "Yes")
hasNumbers = includes(hasNumbers, "y", "Y", "Yes")

special_characters = "`!@#$%^&*()_+=-`[]\|}{';:\",./?><"
alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
characters = ""
if hasSpecialChar:
    if hasNumbers:
        characters = alphabet + numbers + special_characters
        choose = [x for x in range(0,len(characters))]
    else:
        characters = alphabet+numbers
        choose = [x for x in range(0,len())]
else:
    if hasNumbers:
        characters = alphabet+numbers
        choose = [x for x in range(0,len(characters))]
    else:
        characters = alphabet
        choose = [x for x in range(0,len(characters))]
        

password = []
while len(password) < int(length):
    index = choice(choose)
    password.append(characters[index])

print("".join(password))
# for index in range(len(password)):
#     print(password[index], flush=True)