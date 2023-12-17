"""
Conway's Game of Life is a simulation that involves the creation and evolution of simple
cellular automata that obey a set of basic rules.
See more at https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life.
Suppose that the game world is made up of a grid, and that this grid is inhabited by cells.
A cell can be either alive or dead during each "generation", a generation is no more than a turn
in the game of life.
To determine if a spot in a grid is occupied by an alive cell Conway created three rules:
    1. A cell stays alive if it has two or three neighbors.
    2. A cell will be born if there will be exactly three neighbors.
    3. Any cell that doesn't fall in the first two cases will die or stay dead.
    
This particular and basic implementation was heavily inspired by Al Sweigart's Automate the Boring Stuff,
that as always provides great inspiration and starting points for personal projects, more at 
https://inventwithpython.com/bigbookpython/project13.html
"""

import copy
import os
import random
import sys
import time

# Creating constants to store the size of the grid and the state of the cells
WIDTH = 200
HEIGHT = 30

ALIVE = "⚪"
DEAD = " "

# Our little automata will take the form of dictionaries, the key is the (x,y) position on
# the grid and the value is the state (Alive or Dead)
nextCells = {}  # Initializing it empty

# ------------ INITIAL STATE -----------
# Creating a random initial set of cells in the grid that will update with the first
# iteration of the simulation
for col in range(WIDTH):  # Looping over the columns
    for row in range(HEIGHT):  # Looping over the rows
        # Starting the simulation with random alive cells, it will be overwritten by the simulation
        if random.randint(0, 10) == 0:
            nextCells[(col, row)] = ALIVE
        else:
            nextCells[(col, row)] = DEAD

# ------------ SIMULATION -----------
while True:   # The simulation will run below until we force a KeyboardInterrupt
    # Each iteration of the loop is a generation as per Conway's rules

    cells = copy.deepcopy(nextCells)  # Current cells for this generation, copied by nextCells

    # Draw the grid and the cells on the screen
    os.system("cls")  # Clear the screen before drawing the next generation
    for row in range(HEIGHT):
        for col in range(WIDTH):
            print(cells[(col, row)], end="")
    print("Press CTRL + C to stop the simulation.")  # Help to force the KeyboardInterrupt

    # Apply Conway's rules
    # Calculation of neighbours
    for col in range(WIDTH):
        for row in range(HEIGHT):
            # Get the neighbouring coordinates, even if they wrap around the edges of the screen
            # The modulo ensures that exceeding coordinates will be set to positions on the other side of the screen
            left = (col - 1) % WIDTH
            right = (col + 1) % WIDTH
            up = (row - 1) % HEIGHT
            down = (row + 1) % HEIGHT

            # Counting the number of neighbours to the cell we are checking in the iteration
            neighbours = 0
            if cells[(left, up)] == ALIVE:  # If the cell in the (col, row) position is alive add a neighbour
                neighbours += 1
            if cells[(col, up)] == ALIVE:
                neighbours += 1
            if cells[(right, up)] == ALIVE:
                neighbours += 1
            if cells[(left, row)] == ALIVE:
                neighbours += 1
            if cells[(right, row)] == ALIVE:
                neighbours += 1
            if cells[(left, down)] == ALIVE:
                neighbours += 1
            if cells[(col, down)] == ALIVE:
                neighbours += 1
            if cells[(right, down)] == ALIVE:
                neighbours += 1

            # Apply Conway's rules for setting up the next generation
            # 1. A cell with 2 or 3 neighbours stays alive:
            if cells[(col, row)] == ALIVE and (neighbours == 2 or neighbours == 3):
                nextCells[(col, row)] = ALIVE
            # 2. A dead cell with exactly 3 neighbours becomes alive
            elif cells[(col, row)] == DEAD and neighbours == 3:
                nextCells[(col, row)] = ALIVE
            # 3. An alive cell with less than 2 neighbours dies of solitude, with more than three dies of overpopulation.
            # Basically, in every other case than the two above a cell dies or stays dead:
            else:
                nextCells[(col, row)] = DEAD

    # Controlling the simulation with a forced exception
    try:
        # A second before clearing the screen and drawing the next generation to give a sense of motion
        time.sleep(1)
    except KeyboardInterrupt:  # Press CTRL + C to stop the simulation
        print("Conway's Game of Life")
        print("By Edoardo Ferreri @ https://github.com/tacticalParmesan")
        sys.exit()

