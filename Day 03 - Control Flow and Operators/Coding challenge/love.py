print("Welcome to magical love calculator!!!")

first_name = input("Enter the first full name: ")
second_name = input("Enter the second full name: ")

total_name = (first_name + second_name).lower()

t = total_name.count("t")
r = total_name.count("r")
u = total_name.count("u")
e = total_name.count("e")

first_score = t+r+u+e

l = total_name.count("l")
o = total_name.count("o")
v = total_name.count("v")
e = total_name.count("e")

second_score = l+o+v+e

total_score = str(first_score) + str(second_score)

print(f"Your Love score is {total_score}")
