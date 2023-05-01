import random
import networkx as nx

def generate_maze(n):
    maze = [[1] * (n + 1) for _ in range(n + 1)]  # creamos una matriz llena de unos
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1 or i == n or j == n:
                maze[i][j] = 0  # los bordes son paredes
    for i in range(2, n, 2):
        for j in range(2, n, 2):
            maze[i][j] = 0  # hacemos un camino horizontal en cada fila par
    for i in range(2, n, 2):
        wall = random.randrange(2, n, 2)
        maze[i][wall] = 0  # hacemos una pared aleatoria en cada fila par
    for j in range(2, n, 2):
        wall = random.randrange(2, n, 2)
        maze[wall][j] = 0  # hacemos una pared aleatoria en cada columna par
    return maze

def maze_to_graph(maze):
    n = len(maze) - 2  # obtenemos el tamaño del laberinto
    G = nx.Graph()  # creamos un grafo vacío
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if maze[i][j] == 0:  # si es un camino, agregamos una arista
                node = (i, j)
                neighbors = []
                if maze[i - 1][j] == 0:
                    neighbors.append((i - 1, j))
                if maze[i + 1][j] == 0:
                    neighbors.append((i + 1, j))
                if maze[i][j - 1] == 0:
                    neighbors.append((i, j - 1))
                if maze[i][j + 1] == 0:
                    neighbors.append((i, j + 1))
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)
    return G