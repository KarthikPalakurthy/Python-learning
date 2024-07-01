print("Hola!! Welcome to leap year calculator!!!!")
year = int(input("Enter the year: "))

if year%4 == 0:
    if year%100 != 0:
        print("It's a Leap Year!!")
    elif year%400 == 0:
        print("It's a Leap year!!")
    else:
        print("Not a Leap Year!!")
else:
    print("Not a Leap Year!!")
        


