charLength = len(input("What's your name? "))

print(type(charLength))

#If we are try to concatenate an integer with a String, the program throws an error

# print("Your name has" + charLength + " characters")

charLengthNew = str(charLength)      # We converted data type of charLength from int to string and assigned it to new vaiable

print("Your name has " + charLengthNew + " characters!!!")