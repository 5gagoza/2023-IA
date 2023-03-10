edad = int(input('¿Cuál es tu edad?\n'))#input recibe strings pero int lo convierte a entero
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')
else:
	print('Edad no válida.')

#Ejercicio

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres mayor de edad vivo.')
elif edad >= 100 and edad <= 120:
	print('Eres mayor de edad que vio la caida de la union sovietica.')
else:
	print('Edad no válida.')