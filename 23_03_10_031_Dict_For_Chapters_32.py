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
print(teclado1['Precio'])
teclado1['Precio'] = '85'
print(teclado1['Precio'])

for x in teclado2:
	print(x, teclado2[x])

#Ejercicio

for x in teclado1:
	print(x, '=', teclado1[x])