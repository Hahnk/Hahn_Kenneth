h = float(input("Please enter your height"))
w = float(input("Please enter your weight"))
BMI = (703*w)/h**2

def calcbmi():
    global BMI
    if BMI <= 18.5:
        return "Underweight"
    elif BMI >= 18.5 and BMI <= 24.9 :
        return "Normal"
    elif BMI >= 25 and BMI <= 29.9 :
        return "Overweight"
    elif BMI >= 29.9 and BMI <= 34.9:
        return "Obese"
    elif BMI >= 35 and BMI <= 39.9:
        return "Very Obese"
    else:
        return "Morbidly Obese"

condition = calcbmi()
print("Your BMI is ", BMI)
print("You are "+ condition)
