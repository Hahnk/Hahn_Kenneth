
def printf(i,p):
    print("{:<17} \t {:10.2f}".format(i,p))


i1 = input("Please enter Item 1")
p1 = float(input("Please enter the Price"))
      
i2 = input("Please enter Item 2")
p2 = float(input("Please enter the Price"))

i3 = input("Please enter Item 3")
p3 = float(input("Please enter the Price"))
subtotal = p1 + p2 + p3
tax = subtotal * .08
total = subtotal + tax 

print ("<<<<<_recipet_>>>>>")
printf (i1, p1)
printf (i2, p2)
printf (i3, p3)
printf ("subtotal", subtotal )
printf ("tax" , tax )
printf ("Toatal", total )
print ("_______________________")
print (" *Thank you for your money* ")
