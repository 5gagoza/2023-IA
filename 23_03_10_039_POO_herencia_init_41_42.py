class Usuarios:#clase principal
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
		self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

class UsuariosPremium(Usuarios):#subclase que hereda de la clase principal
	frase = ''
	def __init__(self, nombre, apellidos, frase2):#no importa que existan 2 metodos init, se usa el de la subclase
		self.nombre = nombre
		self.apellidos = apellidos
		self.frase2 = frase2
	def imprimir_frase(self):
		print('Frase:', self.frase)
		print('Frase2:', self.frase2)

user = Usuarios('Gabriel', 'Gonzalez Zarate')
user.imprime_datos()

user2 = UsuariosPremium('Gabriel Premium', 'Gonzalez Zarate', 'aprende algo dinero')
user2.frase = 'dinero dinero dinero'
user2.imprime_datos()
user2.imprimir_frase()