height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in Kilos: "))

bmi = round(weight/(height*height), 3)

print(f"The height entered is {height} and the weight entered is {weight}")

if bmi < 18.5:
    print(f"Your BMI value is {bmi} and you are underweight")
elif bmi < 25:
    print(f"Your BMI value is {bmi} and you are normal weight")
elif bmi < 30:
    print(f"Your BMI value is {bmi} and you are slightly over weight")
elif bmi < 35:
    print(f"Your BMI value is {bmi} and you are obese")
else:
    print(f"Your BMI value is {bmi} and you are clinically obese")



