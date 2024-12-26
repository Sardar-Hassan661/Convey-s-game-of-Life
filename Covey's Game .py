import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize grid with random 0s (dead) and 1s (alive)
GRID_SIZE = 50
grid = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE))

# Count the number of alive neighbors for a cell
def count_neighbors(x, y):
    neighbors = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),              (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]
    return sum(grid[i % GRID_SIZE, j % GRID_SIZE] for i, j in neighbors)

# Update grid based on Conway's rules
def update_grid():
    new_grid = grid.copy()
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            alive_neighbors = count_neighbors(x, y)
            if grid[x, y] == 1:  # Alive cell
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[x, y] = 0  # Dies
            else:  # Dead cell
                if alive_neighbors == 3:
                    new_grid[x, y] = 1  # Becomes alive
    return new_grid

# Animation function
def animate(frame):
    global grid
    grid = update_grid()
    mat.set_data(grid)
    return [mat]

# Set up plot
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap="binary")
ax.axis("off")

# Run animation
ani = FuncAnimation(fig, animate, interval=200 , blit=True)
plt.show()