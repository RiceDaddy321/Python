import pygal
from die import Die

# Python code to extract last two digits of a number using Function

def last_digit(number):
    a_string = str(number)
    a_length = len(a_string)
    c = a_string[a_length - 1: a_length]
    return int(c)

def first_digit(number):
    a_string = str(number)
    c = a_string[0:1]
    return int(c)


# Create a D6
die_1 = Die(3141595494)
#die_2 = Die(0)

# MAke some rolls, and store in a list.
results = []
for roll_num in range(5000):
    result = first_digit(die_1.roll_wit_0())
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, 10):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and D10 50000 times."
hist.x_labels = [str(label) for label in range(1, 10)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + d10', frequencies)
hist.render_to_file('die_visual.svg')
print("done")