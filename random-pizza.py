from json import load
from random import choice
from time import sleep

toppings = load(open('toppings.json'))
meats = toppings['meats']
non_meats = toppings['non-meats']

num_meats = int(raw_input("How many meat toppings? "))
num_veggies = int(raw_input("How many non-meat toppings? "))

your_toppings = []
for meat in range(0, num_meats):
    random_meat = choice(meats)
    your_toppings.append(random_meat)
    meats.remove(random_meat)

for non_meat in range(0, num_veggies):
    random_non_meat = choice(non_meats)
    your_toppings.append(random_non_meat)
    non_meats.remove(random_non_meat)

randomized_toppings = your_toppings
for toppings in your_toppings:
    random_topping = choice(your_toppings)
    randomized_toppings.append(random_topping)
    your_toppings.remove(random_topping)

print("Randomizing toppings.....")
sleep(2)
print("\n\nYour toppings are:")
for topping in randomized_toppings:
    print(topping)


