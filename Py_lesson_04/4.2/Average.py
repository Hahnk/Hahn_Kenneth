def calcAvg (n1,n2,n3):
    return ((n1+n2+n3)/3)

def Printll(n1,n2, n3): 
    print("The average of" ,n1,",", n2, ",and", n3 ," is {:.5f}".format(calcAvg(n1,n2,n3)))
    
n1 = float(input("your 1st number"))
n2 = float(input("your 2nd number"))
n3 = float(input("your 3rd number"))

Printll(n1,n2,n3) 
