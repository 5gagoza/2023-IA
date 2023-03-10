def funcion1():
	global num1#variable global
	num1 = 10
	num2 = 2#variable local, no se puede llamar fuera de la funcion

funcion1()#se llama la funcion
print(num1)#se puede mandar a llamar en cualquier parte del codigo

def funcion2():
	pass
	def funcion3():#funcion local en una funcion
		print('String en la función anidada.')
	funcion3()
 
funcion2()

'''
para importar modulos se hace con
import _______
para importar un modulo especifico de otro es
from ____ import___
se puede cambiar el nombre con
import ___ as ___
'''
import math

def area(radio):#funcion normal
	resultado = math.pi * radio * radio
	print(resultado)

area(2)

area2 = lambda radio: (math.pi * radio * radio)
print(area2(2))#funcion lambda
