from __future__ import print_function
from json import load
from random import choice
from time import sleep
from sys import stdout

def get_num_toppings(max_num_toppings):
    try:
        valid_number = False
        while not valid_number:
            num = int(raw_input("There are " + str(max_num_toppings) + 
                " available. How many would you like? "))
            if num < 0 or num > max_num_toppings:
                print("There aren't that many toppings available. Try again...")
                sleep(1)
            else:
                valid_number = True
        return num
    except ValueError:
        print("You must enter a number! Try again...")
        sleep(1)
        return get_num_toppings(max_num_toppings)

def report(option, selection):
    print("{:59}".format("= " + option + selection) + "=")

def print_randomizing():
    print("")
    print("Randomizing choices", end = "")
    stdout.flush()
    for i in range(0, 5):
        print(".", end = "")
        stdout.flush()
        sleep(0.5)
    print("")
    print("")

def print_report(crust, cheese_level, sauce, sauce_level, toppings):
    print_randomizing()
    print("YOUR RANDOM PIZZA")
    print("="*60)
    report("CRUST: ", crust)
    report("CHEESE LEVEL: ", cheese_level)
    report("SAUCE: ", sauce)
    report("SAUCE LEVEL: ", sauce_level)
    report("TOPPINGS: ", "")
    for topping in toppings:
        report("    ", topping)
    print("="*60)
    print("")

def pick_toppings(toppings, num_toppings):
    your_toppings = []
    for topping in range(0, num_toppings):
        random_topping = choice(toppings)
        your_toppings.append(random_topping)
        toppings.remove(random_topping)
    return your_toppings

def pick_options(crusts, cheese_levels, sauces, sauce_levels, toppings, num):
    crust = choice(crusts)
    cheese_level = choice(cheese_levels)
    sauce = choice(sauces)
    sauce_level = choice(sauce_levels)
    my_toppings = pick_toppings(toppings, num)
    return (crust, cheese_level, sauce, sauce_level, my_toppings)

def load_options(file_name = 'options.json'):
    options = load(open(file_name))
    crusts = options['crusts']
    cheese_levels = options['cheese level']
    sauces = options['sauce']
    sauce_levels = options['sauce level']
    toppings = options['toppings']
    return (crusts, cheese_levels, sauces, sauce_levels, toppings)

