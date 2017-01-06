x = input("Please input an expression")
eq = x.split()
print (eq)
# == is CHECKING if they are equal, = sets things equal assignment vs logical
i = 0
while i < len(eq):
    if i < len(eq) and (eq[i] == "*" or eq[i] == "/"):
        if eq[i] == "*":
            eq[i]= int(eq[i-1]) * int(eq[i+1])
        else:
            eq [i]= int(eq[i-1]) / int(eq[i+1])
        eq.pop(i-1)
        eq.pop(i)
    else: 
        i += 1

i = 0
while i < len(eq):
    if i < len(eq) and (eq[i]=="+" or eq[i] == "-"):
        if eq[i] == "+":
            eq[i] = int(eq[i-1])+ int(eq[i+1])
        else:
            eq[i] = int(eq[i-1]) - int(eq[i+1])
        eq.pop(i-1)
        eq.pop(i)
    else:
        i += 1

print(eq)
