import os
import sys

test_file = open("test.txt", "wb")  # can also use "ab+" to open or create the file

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("write me to the file\n", 'UTF-8'))  # You need the bytes and UTF-8 in order to have write stuff to a file

test_file.close()

test_file = open("test.txt", "r+")  # r+ is for reading and writing

text_in_file = test_file.read()
print(text_in_file)

test_file.close()
os.remove("test.txt") #ADVISO NECESITAS CERRRAR EL FILE PARA QUITARLO

with open("mydata.txt", mode="w", encoding="UTF-8") as myFile:
	myFile.write("Hey bro\n")
