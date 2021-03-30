import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plt the points.
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi= 128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")