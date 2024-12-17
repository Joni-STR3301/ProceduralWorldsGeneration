import numpy as np
import matplotlib.pyplot as plt

def diamond_square(size, roughness):
    grid = np.zeros((size, size))
    step_size = size - 1
    grid[0, 0] = grid[0, -1] = grid[-1, 0] = grid[-1, -1] = np.random.rand()

    def square_step(x, y, size, offset):
        avg = (grid[x, y] + grid[x+size, y] + grid[x, y+size] + grid[x+size, y+size]) / 4
        grid[x+size//2, y+size//2] = avg + offset

    def diamond_step(x, y, size, offset):
        half_size = size // 2
        avg = (grid[x-half_size, y] + grid[x+half_size, y] + grid[x, y-half_size] + grid[x, y+half_size]) / 4
        grid[x, y] = avg + offset

    while step_size > 1:
        for x in range(0, size-1, step_size):
            for y in range(0, size-1, step_size):
                square_step(x, y, step_size, np.random.uniform(-roughness, roughness))
        for x in range(0, size-1, step_size//2):
            for y in range((x + step_size//2) % step_size, size-1, step_size):
                diamond_step(x, y, step_size, np.random.uniform(-roughness, roughness))
        step_size //= 2
        roughness /= 2

    return grid

def run():
    size = 129
    terrain = diamond_square(size, roughness=1)
    plt.imshow(terrain, cmap='terrain')
    plt.show()
