import random

#creates the list
xno = []

# Filling the list
for i in range (0,4):
    xno.append([])
    for j in range (0,4):
        switch = random.randint(0,1)
        if switch == 0:
            xno[i].append("X")
        else:
            xno[i].append("O")

#Printing the List
for values in xno:
    output = ""
    for value in values:
        output += value + " "
    print(output)
