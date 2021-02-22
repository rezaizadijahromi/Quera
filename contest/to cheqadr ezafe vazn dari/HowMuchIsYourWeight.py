weight = int(input())
hieght = float(input())

BMI = weight/(hieght*hieght)
round(BMI,2)
if BMI < 18.5:
    print("{:.2f}".format(BMI))
    print("Underweight")
elif BMI >= 18.5 and BMI <= 25:
    print("{:.2f}".format(BMI))
    print("Normal")
elif BMI > 25 and BMI < 30:
    print("{:.2f}".format(BMI))
    print("Overweight")
elif BMI > 30:
    print("{:.2f}".format(BMI))
    print("Obese")