def interest (P,r,n,t) :
    return (P*((1+(r/n))**(n*t))/(t*12))
# The format curly bracket thing can go directly into the print statement, right where it needs to work.
#For return functions, the curly bracket can't go into  the function. 
P = float(input(" Please input principal amount"))
r = float(input(" Please input interest rate"))
n = float(input(" Please input compound rate per year"))
t = float(input(" Please input leangth of loan in years"))
print ("Your total payment due is {:<0.2f}".format (interest(P,r,n,t)),"$") 
