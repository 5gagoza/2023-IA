class Usuario:
	def __init__(self, nombre, apellidos):#para inicializar un objeto con atributos, no vacio
		self.nombre = nombre
		self.apellidos = apellidos

	def imprime_datos(self):#equivalente a la palabra reservada this
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

user = Usuario('Gabriel', 'Gonzalez Zarate')
user.imprime_datos()