mensaje = 'variable string'#se declara la variable y se guarda un string
mensaje = 10#se cambia el valor de la variable a un 10, tambien se cambio el tipo de variable
'''
esto sucede porque las variables actuarian
como un puntero en C en el cual apuntan a un espacio de memoria,
al hacer el cambio de "variable string" a 10
se esta apuntando a un espacio de memoria diferente
'''
print(mensaje + 20)#se realiza una suma dentro del print (no posible si  la variable fuera un string u otro tipo de variable que no fuera iint o float)

#Ejercico

var_mensaje = 'mensaje'

var_num1 = 23
var_num2 = 25

suma = var_num1 + var_num2

print(suma, var_mensaje)
