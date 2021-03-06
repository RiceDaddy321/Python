def make_pizza(size, *toppings):  # tells python to make an empty tuple called toppings
    """Print the list of toppings that have been represented"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def print_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza('pepporoni')
print_pizza('pepporoni', 'mushrooms', 'brot')
