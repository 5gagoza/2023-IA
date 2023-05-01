def alumnos(*args):
	print('el primero es', args[0], 'y el ultimo es', args[-1])

alumnos('pepito', 'melon', 'melames', 'io', 'no se')

#Ejercicio

def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')#4 argumentos
colores('lila', 'negro', 'rojo')#3 argumentos
colores('rosa')#1 argumento
colores('marrón', 'naranja')#2 argumentos

def colores2(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores2('lila', 'cyan')