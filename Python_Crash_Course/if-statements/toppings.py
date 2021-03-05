requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

requested_toppings = ['mushroom', 'onions', 'pineapple']
print("mushroom" in requested_toppings)
print("pepperoni" in requested_toppings)

requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom' in requested_toppings:
    print('Adding musroom')
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('adding extra cheese')

print('finished your pizza')
