for variable in range(1, 5):
   print(variable)
print("-------------------------------")
for variable in range(5, 0, -1):
    print (variable)
print ("-----------------------------")    
for variable in range (0, 10, 2):
    print (variable)
print("------------------------------")

 #str(variable) =" variable values"

#str(10) = 10
# range (min, max, iteration)
output = ""
for variable in range (1,11):
    output = output + str(variable) + ""
print(output)

print("-------------------------------")  

output = ""
for variable in range(10,0,-1):
    output = output + str(variable) + " "
print(output)

print ("-------------------------")

# len() function returns the number of characters in string

word = "COMPSCI"
print(len(word))
#output=7

print ("-------------------------")

#index function to search for character in string, and tell where it is.
#use dot notation
#   stringname.index(<Desired character>)


print(word.index("S"))
#output = 4
print ("-------------------------")

#Slicing strings
#variablename[start:stop]

word=("COMPSCI")

print(word[2])
print(word[1:4])
