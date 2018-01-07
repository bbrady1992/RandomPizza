from random import choice
from json import load

class Pizza:
    def __init__(self):
        self.options_file = 'menus/Dominos.json'
        self.options = None
        self.crust = None
        self.cheese_level = None
        self.sauce = None
        self.sauce_level = None
        self.num_toppings = 3
        self.toppings = None
        self.load_options()

    def load_options(self):
        self.options = load(open(self.options_file))

    def pick_crust(self):
        self.crust = choice(self.options['crusts'])

    def pick_cheese_level(self):
        self.cheese_level = choice(self.options['cheese level'])

    def pick_sauce(self):
        self.sauce = choice(self.options['sauce'])

    def pick_sauce_level(self):
        self.sauce_level = choice(self.options['sauce level'])

    def pick_toppings(self):
        self.toppings = []
        toppings = list(self.options['toppings'])
        for i in range(0, self.num_toppings):
            random_topping = choice(toppings)
            self.toppings.append(random_topping)
            toppings.remove(random_topping)

    def randomize(self):
        self.pick_crust()
        self.pick_cheese_level()
        self.pick_sauce()
        self.pick_sauce_level()
        self.pick_toppings()
