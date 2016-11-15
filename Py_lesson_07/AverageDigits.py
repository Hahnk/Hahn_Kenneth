number = int(input(" Please input some numbers"))
digits = 0
average = 0

def avgDig():
    global digits, average, number
    num = number
    while (num > 0 ):
        digits += 1
        average += num % 10
        num = int(num/10)
    print("The average of the digits in ", number ," is ", average/digits )

avgDig()
