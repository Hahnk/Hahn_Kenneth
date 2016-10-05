def method1 (num):
    return num

def numprint (num):
    print ("method1 returns the number" , method1 (num))

num = 3
numprint (num)



num = 3
num2 = 4
num = 0

def mksum ():
    global sum, num, num2
    sum = num =num2

def numprint ():
    global sum, num, sun2
    print(num, "plus" , num2, "equals" , sum )

mksum()
sumprint ()
