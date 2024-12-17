import random
import numpy as np
import matplotlib.pyplot as plt

TILES = [0, 1, 2]

# Правила соседства (какие плитки могут быть рядом с другими)
ADJACENCY_RULES = {
    0: [0, 2],  # пустая клетка может быть рядом с пустой или дорожкой
    1: [1, 2],  # стена может быть рядом с другой стеной или дорожкой
    2: [0, 1, 2],  # дорожка может быть рядом с любым объектом
}

def is_valid(tile, neighbors):
    """Проверяет, может ли текущая плитка быть рядом с данными соседями"""
    for neighbor in neighbors:
        if neighbor not in ADJACENCY_RULES[tile]:
            return False
    return True

def get_neighbors(grid, x, y):
    """Возвращает соседей для клетки (x, y)"""
    neighbors = []
    if x > 0:
        neighbors.append(grid[x-1, y])
    if x < grid.shape[0] - 1:
        neighbors.append(grid[x+1, y])
    if y > 0:
        neighbors.append(grid[x, y-1])
    if y < grid.shape[1] - 1:
        neighbors.append(grid[x, y+1])
    return neighbors

def collapse_wave_function(grid):
    """Основной алгоритм WFC"""
    possibilities = [[TILES[:] for _ in range(grid.shape[1])] for _ in range(grid.shape[0])]

    while True:
        # Находим клетку с наименьшей неопределённостью
        min_possibilities = float('inf')
        to_collapse = None

        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                if grid[x, y] == -1 and len(possibilities[x][y]) > 0 and len(possibilities[x][y]) < min_possibilities:
                    min_possibilities = len(possibilities[x][y])
                    to_collapse = (x, y)

        if to_collapse is None:
            # Все клетки схлопнулись
            break

        x, y = to_collapse
        if not possibilities[x][y]:
            # Если нет доступных вариантов, можно присвоить значение по умолчанию
            grid[x, y] = random.choice(TILES)
        else:
            # Выбираем случайное возможное состояние для клетки
            tile = random.choice(possibilities[x][y])
            grid[x, y] = tile

        # Обновляем соседей
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == -1:
                # Убираем из возможностей те плитки, которые нарушают правило соседства
                possibilities[nx][ny] = [t for t in possibilities[nx][ny] if is_valid(t, get_neighbors(grid, nx, ny))]

    return grid

def run():
    # Инициализация пустого поля (где -1 означает неопределённую клетку)
    width, height = 10, 10
    grid = np.full((width, height), -1)

    # Запуск алгоритма WFC
    grid = collapse_wave_function(grid)

    # Визуализация результата
    plt.imshow(grid, cmap='terrain')
    plt.colorbar()
    plt.show()
