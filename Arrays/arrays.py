from array import *

myArray = array('i', [1, 2, 3, 4, 5])
print(myArray)

myArray.insert(4, 6)
#print(myArray)

def traverseArray(array):
    for i in array:
        print(i)

filee = 'Arrays/res.txt'
outputFile = "questions.txt"

resul = []
with open(filee, 'r') as file:

    for line in file:
        print(line)
        if line[0] == "#":
            resul.append(line)

with open(outputFile, 'w') as file:

    for line in resul:
        file.writelines(line)