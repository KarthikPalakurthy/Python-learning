import random

print("Who Pays the bill???")

names_string = input("Enter the names seperated by a comma: ")

names = names_string.split(",")

total_members = len(names)

# print(total_members)          # Debugging here

random_person = random.randint(0, total_members - 1)

print(f"{names[random_person]} pays the bill today!!!!!")