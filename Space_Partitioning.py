import random
import matplotlib.pyplot as plt

class Room:
    def __init__(self, x, y, width, height):
        self.x, self.y, self.width, self.height = x, y, width, height

def split_room(x, y, width, height, min_size=5):
    if width <= min_size * 2 or height <= min_size * 2:
        return [Room(x, y, width, height)]
    
    horizontal = random.choice([True, False])
    if horizontal:
        split = random.randint(min_size, height - min_size)
        return split_room(x, y, width, split) + split_room(x, y + split, width, height - split)
    else:
        split = random.randint(min_size, width - min_size)
        return split_room(x, y, split, height) + split_room(x + split, y, width - split, height)

def run():
    rooms = split_room(0, 0, 50, 50)
    for room in rooms:
        plt.gca().add_patch(plt.Rectangle((room.x, room.y), room.width, room.height, edgecolor='black', facecolor='gray'))

    plt.xlim(0, 50)
    plt.ylim(0, 50)
    plt.gca().set_aspect('equal')
    plt.show()
