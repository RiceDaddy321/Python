cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'audi'
#makes sure that this always work no matter the formatting
print(cars.lower() == 'audi')
