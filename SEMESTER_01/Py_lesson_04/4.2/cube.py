def calcsa (si, sa):
    return (6*(si**2))

def Printll(si,sa): 
    print("The surface area of a cube with" ,si, "sides is{:.5f}".format(calcsa(si,sa)))

    
si = float(input("Please enter the number of sides"))
sa = calcsa

Printll(si, sa) 
