print("Welcome to Pizza order!!!")

size = input("Enter the PIzza Size? S, M or L: ")

toppings = input("Extra tippoings Y or N: ")

cheese = input("Extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if toppings == "Y":
        bill +=2
    if cheese == "Y":
        bill += 1
    print(f"Your final bill is £{bill}")

elif size == "M":
    bill = 20
    if toppings == "Y":
        bill += 3
    if cheese == "Y":
        bill +=1
    print(f"Your final bill is £{bill}")

else: 
    bill = 25
    if toppings == "Y":
        bill += 3
    if cheese == "Y":
        bill +=1
    print(f"Your final bill is £{bill}")