def printf(i,p):
    print("* {:<6} \t {:>15} *".format(i,p))

FN = input("Enter your first name: ")
LN = input("Enter your last name: ")
TL = input ("Enter your title:")
SS = input ("Enter the school site: ")
SY = input ("Enter the school year: ")
SJ = input ("What is your subject? ")


print ("**********************************")
printf(FN,LN)
printf(TL,SS)
printf(SY,SJ)
print ("**********************************")
