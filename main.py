# import random module
import random

names_string = input("Enter the names: ")

names = names_string.split(", ")
# print(f"{names} are successfully registered!")

# Get the total number of items in list
num_items = len(names)

# Generate random numbers between 0 and the last index.
rand_choice = random.randint(0, num_items - 1)

# Pick out random person from list of names using the random number.
person_who_will_pay = names[rand_choice]

print(f"{person_who_will_pay} is going to buy the meal today!")