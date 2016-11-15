number = int(input("Please input a number"))

def getRev():
    num = number
    rev = 0
    while num > 0:
        rev *= 10
        rev += num % 10
        num = int(num/10)
    print (number, " reversed is ", rev)

getRev()
