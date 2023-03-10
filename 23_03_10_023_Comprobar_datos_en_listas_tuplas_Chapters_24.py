navegadores = ['chrome', 'firefox', 'opera', 'safari']
print('chrome' in navegadores)
print('chrome2' in navegadores)

#Ejercicio

tupla = ('rojo', 'azul', 'verde', 'amarillo')
entrada = input('Introduce el nombre de un color: ')
if entrada in tupla:
    print('El color ' + entrada + ' esta en la tupla')
else:
    print('color no valido')