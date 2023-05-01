import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()  # nodos visitados
    queue = deque([start])  # cola de nodos por visitar

    # Mientras queden nodos por visitar
    while queue:
        vertex = queue.popleft()  # sacamos el primer nodo de la cola
        if vertex not in visited:
            visited.add(vertex)  # lo marcamos como visitado
            #print(vertex)  # imprimimos el nodo
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)  # agregamos los vecinos no visitados a la cola

    return visited

# Creamos el grafo
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')])

# Dibujamos el grafo
pos = nx.spring_layout(G)  # posición de los nodos
nx.draw_networkx_nodes(G, pos, node_color='lightblue')  # dibujamos los nodos
nx.draw_networkx_edges(G, pos, edge_color='gray')  # dibujamos las aristas
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')  # etiquetamos los nodos

# Realizamos la búsqueda en anchura y mostramos los nodos visitados
print("Nodos visitados:")
print(bfs(G, 'A'))

plt.axis('off')  # ocultamos los ejes
plt.show()  # mostramos el grafo
