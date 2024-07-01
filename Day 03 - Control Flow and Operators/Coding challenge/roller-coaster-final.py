print("Welcome to the Roller Coaster!!!")

height = int(input("What's your height in cms? "))

if height >= 120:
    age = int(input("Enter your age? "))
    if age <12:
        bill = 8
        print("Tickets are £8")
    elif age <=18:
        bill = 11
        print("Tickets are £11")
    else:
        bill =15
        print("Tickets are £15")
    
    photo_needed = input("Do you need a photo? (Y/N) ")
    
    if photo_needed == "Y":
        bill += 3

    print(f"Your final bill is £{bill}")
else:
    print("Sorry, got to be bit more taller :( ")