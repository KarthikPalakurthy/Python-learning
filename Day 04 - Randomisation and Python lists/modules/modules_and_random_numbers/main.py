import random
import my_module   # We are importing the my_module module here....


# random_var = random.randint(1,100)    # Generates a Random number b/w 1 and 99
random_var = random.random()            # Generates a random float value b/w 0.000001 - 0.999999

print(random_var)

# Now we preform some random operations using the variables from my_module.py
print(my_module.my_second)
print(my_module.my_third * random_var)