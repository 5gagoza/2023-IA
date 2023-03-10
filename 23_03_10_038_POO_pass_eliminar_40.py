class NombreClase:#clase vacia
	pass

class Usuario:
	def __init__(self, nombre, apellidos):#para inicializar un objeto con atributos, no vacio
		self.nombre = nombre
		self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
	def eliminar_apellidos(self):
		del self.apellidos#eliminar atributos
  
user = Usuario('Gabriel', 'Gonzalez Zarate')
user.imprime_datos()
user.eliminar_apellidos()
del user #eliminar objeto