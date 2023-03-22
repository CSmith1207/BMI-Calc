def BMICalc(feet, inches, pounds):
    ft = float(feet)
    inc = float(inches)
    lbs = float(pounds)
    BMI = 0

    #Convert from lbs to kg
    lbs *= 0.45

    #Convert from in to m
    inc = (ft * 12 + inc) * 0.025

    #Square the answer from the prev step
    BMI = inc * inc

    #Divide the answer from step 1 by the answer from step 3
    BMI = lbs/BMI

    #Round the answer to 1 decimal place
    return round(BMI, 1)

def BMICategory(BMI):
    print("\nYour BMI is", BMI)

    if BMI < 18.5:
        return "You are underweight"
    elif BMI < 25:
        return "You are normal weight"
    elif BMI < 30:
        return "You are overweight"
    else:
        return "You are obese"

print("Enter your height in feet and inches and your weight in pounds")

ft = input("Feet: ")
inc = input("Inches: ")
lbs = input("Pounds: ")
BMI = BMICalc(ft, inc, lbs)

print(BMICategory(BMI))
