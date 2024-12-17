import numpy as np
import pygame
import random

# Инициализация pygame
pygame.init()

# Размер окна и клеток
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Константы для карты
ROOM_COUNT = 10  # Количество комнат
ROOM_MIN_SIZE = 5  # Минимальный размер комнаты
ROOM_MAX_SIZE = 10  # Максимальный размер комнаты

# Генерация подземелья
class DungeonGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dungeon_map = np.full((height, width), '.', dtype='<U1')
        self.rooms = []

    def generate(self):
        self.generate_rooms()
        self.connect_rooms()
        return self.dungeon_map

    def generate_rooms(self):
        for _ in range(ROOM_COUNT):
            room_width = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            room_height = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            room_x = random.randint(1, self.width - room_width - 1)
            room_y = random.randint(1, self.height - room_height - 1)

            new_room = (room_x, room_y, room_width, room_height)
            self.rooms.append(new_room)

            # Отметить комнату на карте
            for y in range(new_room[1], new_room[1] + new_room[3]):
                for x in range(new_room[0], new_room[0] + new_room[2]):
                    self.dungeon_map[y, x] = 'R'

    def connect_rooms(self):
        for i in range(1, len(self.rooms)):
            room1 = self.rooms[i - 1]
            room2 = self.rooms[i]

            # Проводим коридор от центра первой комнаты к центру второй комнаты
            start_x, start_y = room1[0] + room1[2] // 2, room1[1] + room1[3] // 2
            end_x, end_y = room2[0] + room2[2] // 2, room2[1] + room2[3] // 2

            # Проводим вертикальный коридор
            if start_x != end_x:
                for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                    self.dungeon_map[start_y, x] = 'C'
            
            # Проводим горизонтальный коридор
            if start_y != end_y:
                for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                    self.dungeon_map[y, end_x] = 'C'

# Рисование карты подземелья
def draw_dungeon(window, dungeon_map):
    window.fill(WHITE)
    
    for y in range(dungeon_map.shape[0]):
        for x in range(dungeon_map.shape[1]):
            cell = dungeon_map[y, x]
            
            # Отображение символов
            if cell == 'R':
                color = BROWN  # Комната
            elif cell == 'C':
                color = GREEN  # Коридор
            else:
                color = WHITE  # Пустое место
            
            pygame.draw.rect(window, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(window, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    pygame.display.flip()

def main():
    # Инициализация окна pygame
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Dungeon Generator")

    # Генерация подземелья
    dungeon_generator = DungeonGenerator(width=40, height=30)
    dungeon_map = dungeon_generator.generate()

    # Главный цикл игры
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовываем подземелье
        draw_dungeon(window, dungeon_map)
        
    pygame.quit()

if __name__ == "__main__":
    main()
