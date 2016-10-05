#Define the calculation perimeter, and two variables, return and tab, then put
#returnm, and the function you want it to work 

def calcPerim (leng, widt):
    return ((2*leng)+(2*widt))

# Then define another print function. return and tab in just the print statement
# from there, just put in the format statement you want it to be, and
# call the previous work function, and its parameters. 



#To format, form is {: number of spaces you want it moved and <, >, or ' for
#left, right, center 
def Printll(l, w): 
    print("Your rectangle is {:.5f}".format(calcPerim(l, w)), "sq ft around.")

#REMEMBER TO  FLOAT IT        
L = float(input("Please enter Length"))
W = float(input("Please enter Width"))

Printll(L,W) 


# The parameters see what the respective variables are around the comma and
#transfer the value, not the variable.  The Parameters of the function and the
#variables in said function have to match up, but oustide of
#functions, it is just related based on the side of the comma.
