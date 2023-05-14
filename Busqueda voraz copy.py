import pygame
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from queue import PriorityQueue
import heapq

# Definir las constantes de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

# Definir los colores
START = (0, 255, 0)
GOAL = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 128, 0)
VIOLET = (175, 0, 255)
VINE = (86, 7, 12)
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def generate_maze(n):
    maze = [[1] * (n + 1) for _ in range(n + 1)]  # creamos una matriz llena de unos
    p = 0.3
    for i in range(1, n, 2):
        for j in range(1, n, 2):
            maze[i][j] = random.choices([0, 1], weights = [0.6, 0.4])[0]  # hacemos un camino horizontal en cada fila par
            if maze[i][j] == 1 and (maze[i + 1][j + 1] == 1 or maze[i + 1][j - 1] == 1 or maze[i - 1][j + 1] == 1 or maze[i - 1][j - 1] == 1):
                maze[i][j] = 0
            maze[i + 1][j] = random.choices([0, 1], weights=[1 - p, p])[0]
            maze[i - 1][j] = random.choices([0, 1], weights=[1 - p, p])[0]
            maze[i][j + 1] = random.choices([0, 1], weights=[1 - p, p])[0]
            maze[i][j - 1] = random.choices([0, 1], weights=[1 - p, p])[0]
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
                    G.add_edge(node, neighbor, weight = random.randrange(1, 100))
    return G

import heapq

def a_star_search(graph, start, goal):
    """
    Realiza una búsqueda de camino en un grafo utilizando el algoritmo A*.
    graph: un diccionario de listas de adyacencia que representa el grafo
    start: el nodo inicial
    goal: el nodo objetivo
    heuristic_fn: una función heurística que estima el costo restante desde un nodo hasta el objetivo
    """
    # Creamos un conjunto de nodos explorados y un diccionario para realizar el seguimiento de los costos
    explored = set()
    cost_so_far = {start: 0}
    came_from = {start: None}
    # Creamos una cola de prioridad para los nodos por explorar, con el nodo inicial como el primero
    frontier = [(heuristic_fn(start, goal), start)]
    
    while frontier:
        # Sacamos el nodo de la cola de prioridad que tenga el menor costo total estimado (f)
        _, current = heapq.heappop(frontier)
        # Si hemos llegado al objetivo, devolvemos el camino
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, cost_so_far[goal]
        # Marcamos el nodo actual como explorado
        explored.add(current)
        # Para cada vecino del nodo actual
        for neighbor, cost in graph[current]:
            # Si el vecino ya ha sido explorado, lo ignoramos
            if neighbor in explored:
                continue
            # Calculamos el costo actual para llegar al vecino desde el nodo inicial
            new_cost = cost_so_far[current] + cost
            # Si el vecino no está en la cola de prioridad o si el nuevo costo es menor que el costo anterior
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                # Actualizamos el costo y el nodo padre del vecino
                cost_so_far[neighbor] = new_cost
                # Actualizamos la cola de prioridad con el nuevo costo total estimado (f)
                priority = new_cost + heuristic_fn(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
    
    # Si no se encuentra un camino al objetivo, devolvemos None
    return None, None


def heuristic_fn(node, goal_node):
    node_x, node_y = node
    goal_x, goal_y = goal_node
    return abs(node_x - goal_x) + abs(node_y - goal_y)

# Dibujar la cuadrícula
def draw_grid(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 9:
                color = START
            elif maze[row][col] == 8:
                color = GOAL
            elif maze[row][col] == 4:
                color = VINE
            elif maze[row][col] == 1:
                color = BLACK
            elif maze[row][col] == 2:
                color = ORANGE
            elif maze[row][col] == 3:
                color = VIOLET
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

maze = generate_maze(20)

G = maze_to_graph(maze)

pos = nx.spring_layout(G)  # posición de los nodos
nx.draw_networkx_nodes(G, pos, node_color='lightblue')  # dibujamos los nodos
nx.draw_networkx_edges(G, pos, edge_color='black')  # dibujamos las aristas
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')  # etiquetamos los nodos
nx.draw_networkx_edge_labels(G, pos, edge_labels = nx.get_edge_attributes(G, 'weight'))


plt.axis('off')  # ocultamos los ejes

plt.show()  # mostramos el grafo
Start = list(G.nodes())[random.randrange(1, G.number_of_nodes())]
Goal = list(G.nodes())[random.randrange(1, G.number_of_nodes())]

maze[Start[0]][Start[1]] = 9
maze[Goal[0]][Goal[1]] = 8
    
path = a_star_search(G, Start, Goal)

if path:
    print('Camino encontrado desde {} hasta {}: {}'.format(Start, Goal, path))
else:
    print('No se encontró un camino desde {} hasta {}'.format(Start, Goal))