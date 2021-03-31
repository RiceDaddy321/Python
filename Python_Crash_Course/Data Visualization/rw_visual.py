import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plt the points.
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth = 8) #c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1
        
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        print("break")
        break
