import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')])

# Dibujamos el grafo
pos = nx.spring_layout(G)  # posición de los nodos
nx.draw_networkx_nodes(G, pos, node_color='lightblue')  # dibujamos los nodos
nx.draw_networkx_edges(G, pos, edge_color='gray')  # dibujamos las aristas
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')  # etiquetamos los nodos

plt.axis('off')  # ocultamos los ejes
plt.show()  # mostramos el grafo
