import random

def generate_maze(n):
    maze = [[1] * (n + 1) for _ in range(n + 1)]  # creamos una matriz llena de unos

    for i in range(1, n, 2):
        for j in range(1, n, 2):
            maze[i][j] = 0  # hacemos un camino horizontal en cada fila par
    for i in range(1, n):
        wall = random.randrange(1, n, 2)
        maze[i][wall] = 0  # hacemos una pared aleatoria en cada fila par
    for j in range(1, n):
        wall = random.randrange(2, n, 2)
        maze[wall][j] = 0  # hacemos una pared aleatoria en cada columna par
    return maze

maze = generate_maze(10)  # generamos un laberinto de tamaño 10x10
for row in maze:
    print(row)  # imprimimos el laberinto
