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
#Top of the range is again, exclusive. The bottom of the list is inclusive
print("----------------------------------------------------")
# i = each item in my list
output = ""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList)-1: # as long as we are one back from the end, we can add a comma
        output += ", "
        j+=1 #to advance the j though the list


    print(output)

print("--------------------------------------------------------")

#You can also quickly and easily add values and append your Lists....

myList = [] #starts empty
for i in range (0, 8):
    myList.append(i*4)# for in range from 0 to 8, add into the list i*4
    output = ""
    j = 0
    for i in myList:
        output+= str(i) #whatever I come up wuth becomes string
        if j < len(myList):
            output += ", "
            j += 1
print(output)



print ("----------------------------------------------------------")


#You can use split() to add values to your array,
#while eliminating unwanted characters using a delimiter.
#Whatever you enter into the parentheses of split(),  (SEE***)
#it will omit this character from it's output entirely.
mylist = []
word = "P r o f e s s o r"
mylist = word.split(" ")
print(mylist)

print ("------------------------------")
word = "P r o f e s s o r"
myList = word.split(" ") # in here
output = ""
for i in myList:
    output += (i)

print(output)



