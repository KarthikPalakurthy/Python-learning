# Calcularing the BMI of an individual, Formula BMI = weight in kilos/height*height in meters

height = float(input())
weight = int(input())

bmi = weight/(height*height)

print("Your BMI is " + str(bmi))