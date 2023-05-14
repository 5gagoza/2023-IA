import pygame
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from queue import PriorityQueue

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

def greedy_search(graph, start_node, goal_node):
    """Función para realizar la búsqueda voraz en un grafo."""
    
    visited_nodes = set()  # Conjunto de nodos visitados
    current_node = start_node  # Nodo actual es el nodo inicial
    
    while current_node != goal_node:
        time.sleep(0.05)
        maze[current_node[0]][current_node[1]] = 2
        if current_node == Start:
            maze[current_node[0]][current_node[1]] = 9 
        draw_grid(maze)
        visited_nodes.add(current_node)  # Añade el nodo actual a los nodos visitados
        neighbors = graph[current_node]  # Obtiene los vecinos del nodo actual
        heuristic_values = {node: heuristic(node, goal_node) for node in neighbors if node not in visited_nodes}  # Calcula el valor heurístico para cada vecino no visitado
        #print(heuristic_values)
        for i in heuristic_values:
            time.sleep(0.05)
            maze[i[0]][i[1]] = 3
            draw_grid(maze)
        if not heuristic_values:  # Si no hay vecinos no visitados, la búsqueda termina sin éxito
            return None
        current_node = min(heuristic_values, key=heuristic_values.get)  # Elige el vecino con menor valor heurístico como nuevo nodo actual
        time.sleep(0.5)
        maze[current_node[0]][current_node[1]] = 4
        # Dibujar la cuadrícula
        draw_grid(maze)
    visited_nodes.add(current_node)  # Añade el nodo objetivo a los nodos visitados
    
    for i in visited_nodes:
        time.sleep(0.5)
        maze[i[0]][i[1]] = 4
        # Dibujar la cuadrícula
        draw_grid(maze)
        
    return visited_nodes  # Devuelve el conjunto de nodos visitados

def heuristic(node, goal_node):
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
    
path = greedy_search(G, Start, Goal)

if path:
    print('Camino encontrado desde {} hasta {}: {}'.format(Start, Goal, path))
else:
    print('No se encontró un camino desde {} hasta {}'.format(Start, Goal))