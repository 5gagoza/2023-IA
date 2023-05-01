# Definición del grafo
grafo = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

# Función de búsqueda en profundidad iterativa
def buscar_profundidad_iterativa(grafo, inicio, objetivo):
    for profundidad_limite in range(len(grafo)):
        visitados = set()
        if buscar_profundidad(grafo, inicio, objetivo, profundidad_limite, visitados):
            return True
    return False

# Función de búsqueda en profundidad
def buscar_profundidad(grafo, actual, objetivo, profundidad_limite, visitados):
    if actual == objetivo:
        return True
    if profundidad_limite <= 0:
        return False
    visitados.add(actual)
    for vecino in grafo[actual]:
        if vecino not in visitados:
            if buscar_profundidad(grafo, vecino, objetivo, profundidad_limite - 1, visitados):
                return True
    return False

# Ejemplo de uso
inicio = 'A'
objetivo = 'F'
resultado = buscar_profundidad_iterativa(grafo, inicio, objetivo)
print(resultado)
