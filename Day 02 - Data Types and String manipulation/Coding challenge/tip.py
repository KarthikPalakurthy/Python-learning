# Tip calculator

print("Welcome to Tip calculator!!!")
total_bill = input("What's your total bill? $")

total_bill_float = float(total_bill)

tip_amount = input("How much would you like to tip in percentage? ")

tip_amount_percent = float(tip_amount)/100

tip_amount_float = float(tip_amount_percent)

total_tip = total_bill_float * tip_amount_float

number_of_people = input("Enter the number of people to split with: ")

people = int(number_of_people)

final_bill = round((total_bill_float + total_tip)/people , 2 )

print(f"The final bill is {final_bill}")

