teclado = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
print(teclado, len(teclado))
del teclado['Precio']
print(teclado)
teclado['color'] = 'negro'
print(teclado)

#Ejercicio

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])