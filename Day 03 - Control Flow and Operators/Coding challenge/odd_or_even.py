print("Odd or Even number checker")
number = int(input("Please enter any number: "))

reminder = number%2    # The Modulo gives the reminder after a division.

if reminder == 0:
    print("The number is Even!!!")
else:
    print("It's an Odd Number!!")