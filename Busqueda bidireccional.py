import pygame
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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
                    G.add_edge(node, neighbor)
    return G

def bfs(graph, start, goal):
    visited = set()  # nodos visitados
    queue = deque([(start, None)])  # cola con el nodo inicial y su padre
    parents = {start: None}  # diccionario con los padres de cada nodo en el camino
    
    # Mientras queden nodos por visitar
    while queue:
        time.sleep(0.05)
        #print(queue)
        vertex, parent = queue.popleft()  # sacamos el primer elemento de la cola
        if vertex not in visited:
            visited.add(vertex)  # lo marcamos como visitado
            parents[vertex] = parent
            #print('v', vertex)  # imprimimos el nodo
            maze[vertex[0]][vertex[1]] = 2
            if vertex == Start:
              maze[vertex[0]][vertex[1]] = 9  
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.extend([(neighbor, vertex)])  # agregamos los vecinos no visitados a la cola
                    maze[neighbor[0]][neighbor[1]] = 3
                        
            if vertex == goal:
                # se encontró el nodo objetivo, construimos el camino de regreso
                path = []
                current = vertex
                
                while current is not None:
                    time.sleep(0.05)
                    maze[current[0]][current[1]] = 4
                    path.append(current)
                    current = parents[current]
                    draw_grid(maze)
                    
                return path[::-1]  # invertimos la lista para obtener el camino de inicio a fin
            
        # Dibujar la cuadrícula
        draw_grid(maze)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                return

    return None

def bidirectional_bfs(graph, start, end):
    forward_queue = deque([(start, [])])
    backward_queue = deque([(end, [])])

    forward_visited = set()
    backward_visited = set()

    while forward_queue and backward_queue:
        time.sleep(0.05)
        forward_node, forward_path = forward_queue.popleft()
        backward_node, backward_path = backward_queue.popleft()
        #print(forward_node)
        if forward_node in backward_visited:
            for i in forward_path + backward_path[::-1]:
                time.sleep(0.05)
                maze[i[0]][i[1]] = 4
                draw_grid(maze)
            return forward_path + backward_path[::-1]

        if backward_node in forward_visited:
            for i in backward_path + forward_path[::-1]:
                time.sleep(0.05)
                maze[i[0]][i[1]] = 4
                draw_grid(maze)
            return backward_path + forward_path[::-1]

        forward_visited.add(forward_node)
        backward_visited.add(backward_node)

        maze[forward_node[0]][forward_node[1]] = 2
        maze[backward_node[0]][backward_node[1]] = 2
        
        if forward_node == Start:
              maze[forward_node[0]][forward_node[1]] = 9
        if backward_node == Goal:
              maze[backward_node[0]][backward_node[1]] = 8 

        for neighbor in graph[forward_node]:
            if neighbor not in forward_visited:
                forward_queue.extend([(neighbor, forward_path + [neighbor])])
                maze[neighbor[0]][neighbor[1]] = 3
                
        for neighbor in graph[backward_node]:
            if neighbor not in backward_visited:
                backward_queue.extend([(neighbor, backward_path + [neighbor])])
                maze[neighbor[0]][neighbor[1]] = 3
        draw_grid(maze) 
    return None


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


plt.axis('off')  # ocultamos los ejes

plt.show()  # mostramos el grafo
Start = list(G.nodes())[random.randrange(1, G.number_of_nodes())]
Goal = list(G.nodes())[random.randrange(1, G.number_of_nodes())]

maze[Start[0]][Start[1]] = 9
maze[Goal[0]][Goal[1]] = 8

path = bidirectional_bfs(G, Start, Goal)


if path:
    print('Camino encontrado desde {} hasta {}: {}'.format(Start, Goal, path))
else:
    print('No se encontró un camino desde {} hasta {}'.format(Start, Goal))