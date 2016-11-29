myList = ["Freddy", "Mike","Lisa","Ellen","Melissa"]

output = ""
for i in myList:
   output += i + " "

print(output)

print("------------------------------------------------")

myList = [1, 2, 3, 4, 5]

print(myList[2])
print(myList[:2])
print(myList[2:3])
print(myList)
print("----------------------------------------------------")

output = ""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList)-1:
        output += ", "
        j+=1


    print(output)
