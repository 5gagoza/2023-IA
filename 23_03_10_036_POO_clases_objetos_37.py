class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

user = Usuario()

user.nombre = 'Gabriel'
user.apellidos = 'Gonzalez Zarate'

user.imprime_datos()