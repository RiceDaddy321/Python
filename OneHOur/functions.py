import sys


def addNumbers(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


print(addNumbers(1, 4))

print("What's your name?")

name = sys.stdin.readline()

print('Hello', name)
