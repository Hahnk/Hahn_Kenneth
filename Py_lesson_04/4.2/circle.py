import math;
# To add math things like pi, you need to import
def calcarea (R):
    return (math.pi*(R**2))

def Printll(R,A): 
    print("The area of a circle with a radius of" ,R, "is {:.5f}".format(calcarea(R)))

    
R = float(input("Please enter the radius of the circle"))
A = calcarea

Printll(R,A) 
