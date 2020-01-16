# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

# reduce problem to string of rights(r) and downs(d). number of r and d must = length of square grid side
# e.g. 2x2 grid could be rrdd, rdrd, rddr, drrd, ddrr, drdr
# they have to be ordered uniquely (no repetitions)

# take number of steps in route (grid side length*2), see how many of those steps need to be "down" steps
# we have "number_Steps" for first to change to "down" , after that we have "number_steps-1" options for next "down"
# repeat this for the number of steps that need to change direction (in this case, equal to length of grid side)
# short way of calculation this is
# (grid_side_length*2)!/grid_side_length!

# the changes can be written in any order so we need to remove the permutaitons of the changes by dividing by grid_side_length!

# full formula:
# (grid_side_length*2)!/grid_side_length!/grid_side_length!

import math

def number_routes(grid_size):
    return math.factorial(grid_size*2)/math.factorial(grid_size)/math.factorial(grid_size)

print(number_routes(20))