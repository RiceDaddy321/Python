# dictionaries are a collection of key-value pairs
# dictionaries are dynamic structures
# you can create empty dictionaries
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
del alien_0['points']
print(alien_0)

alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien['x_position']))

# Move the alien to the right
# Determine how far to move the based on its current speed.
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment.
alien['x_position'] = alien['x_position'] + x_increment

print("New x-position: " + str(alien['x_position']))
