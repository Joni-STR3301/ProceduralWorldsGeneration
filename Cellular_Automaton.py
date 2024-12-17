import numpy as np
import matplotlib.pyplot as plt

def generate_map(width, height, fill_prob=0.4):
    grid = np.random.choice([0, 1], size=(width, height), p=[1-fill_prob, fill_prob])
    return grid

def apply_cellular_automaton(grid, iterations=5):
    for _ in range(iterations):
        new_grid = grid.copy()
        for x in range(1, grid.shape[0] - 1):
            for y in range(1, grid.shape[1] - 1):
                alive_neighbors = np.sum(grid[x-1:x+2, y-1:y+2]) - grid[x][y]
                if grid[x][y] == 1:
                    if alive_neighbors < 4:
                        new_grid[x][y] = 0
                else:
                    if alive_neighbors > 4:
                        new_grid[x][y] = 1
        grid = new_grid
    return grid

def run():
    map_grid = generate_map(100, 100)
    cave_map = apply_cellular_automaton(map_grid)
    plt.imshow(cave_map, cmap='gray')
    plt.show(block=True)