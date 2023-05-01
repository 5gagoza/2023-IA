x = 1
while x <= 10:
	print(x)
	if x == 5:
		break
	x += 1
x = 0
while x < 10:
	x += 1
	if x == 5 or x == 7:#Se salta el print en estas 2 condiciones
		continue
	print(x)
 
 #Ejercicio

x = 0
while x <= 30:
	x += 1
	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor', x, 'de x')
		continue

	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía', x)
		break
	print('El valor del bucle es:', x)
	
 