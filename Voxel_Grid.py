import numpy as np
import matplotlib.pyplot as plt

def generate_voxel_world(size):
    world = np.random.randint(2, size=(size, size))
    return world

def run():
    voxel_world = generate_voxel_world(50)
    plt.imshow(voxel_world, cmap='gray')
    plt.show()
