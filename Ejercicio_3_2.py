class Car():
	"""Clase tipo coche""" 
	def __init__(self, make, model, year): 
		"""Inicializacion de los atributos""" 
		self.make = make 
		self.model = model 
		self.year = year 
		self.odometer_reading = 0
	def get_descriptive_name(self):
		""" Imprime las caracteristicas en la pantalla""" 
		long_name = str(self.year)+' '+self.make + ' '+self.model 
		return long_name.title()
	def read_odometer(sefl):
		"""Imprime los kilometros recorrido por el auto""" 
		print("This car has " + str(sefl.odometer_reading) + " miles on it")
my_new_car = Car('mustang','shelby',2020) 
print(my_new_car.get_descriptive_name()) 
my_new_car.read_odometer()