number = int(input("Please intput a number"))

def sumdigits():
    global summ,num
    num = number
    summ = 0
    while (num > 0):
            summ += (num % 10)
            num = int(num/10)

sumdigits()
print("The sum of the digits in ", number, "is ",summ)
