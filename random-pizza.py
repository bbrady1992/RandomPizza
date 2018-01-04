from utils import *

def generate_random_pizza():
    print("")
    crusts, cheese_levels, sauces, sauce_levels, toppings = load_options()
    num_toppings = get_num_toppings(len(toppings))
    crust, cheese_level, sauce, sauce_level, my_toppings = pick_options(crusts,
            cheese_levels, sauces, sauce_levels, toppings, num_toppings)
    print_report(crust, cheese_level, sauce, sauce_level, my_toppings)

if __name__ == "__main__":
    generate_random_pizza()
