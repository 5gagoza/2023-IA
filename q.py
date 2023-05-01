import networkx as nx
import matplotlib.pyplot as plt

# Define el grafo de ejemplo
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'), ('J', 'K'), ('K', 'L'), ('L', 'A')])

# Define la función de búsqueda en profundidad con start y goal
def dfs(graph, start, goal):
    visited = set()    # conjunto para almacenar los nodos visitados
    path = []           # lista para almacenar el camino encontrado
    
    dfs_recursive(graph, start, visited, path, goal)
    
    if goal not in path:
        print(f"No se encontró un camino de {start} a {goal}")
    else:
        print(f"Camino encontrado de {start} a {goal}: {path}")
    
def dfs_recursive(graph, node, visited, path, goal):
    visited.add(node)  # agregamos el nodo actual al conjunto de nodos visitados
    path.append(node)  # agregamos el nodo actual al camino
    
    if node == goal:   # si hemos llegado al objetivo, retornamos el camino
        return path
    
    for neighbor in graph.neighbors(node):  # recorremos los vecinos del nodo actual
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, visited, path, goal)  # llamamos recursivamente la función para el vecino no visitado
            if result is not None:  # si se encontró el objetivo en el camino, retornamos el camino
                return result
    
    path.pop()  # eliminamos el último nodo del camino, ya que no lleva al objetivo

# Ejemplo de uso
start_node = 'A'
goal_node = 'H'

dfs(G, start_node, goal_node)

# Dibujamos el grafo
nx.draw(G, with_labels=True)
plt.show()
