color = ['rojo', 'azul', 'verde', 'amarillo']
print(color)
color.pop()
print(color)
eliminado = color.pop(1)
print(eliminado, color)

#Ejecicio

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa','blanco', 'naranja']

print(colores)

eliminados = []

eliminados.append(colores.pop(1))
eliminados.append(colores.pop(7))

print(colores, eliminados)
