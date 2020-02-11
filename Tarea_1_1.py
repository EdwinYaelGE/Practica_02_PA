class restaurant():
	"""Clase tipo restaurante""" 
	def __init__(self,restaurant_name,restaurant_type,restaurant_OC): 
		"""Inicializacion de los atributos""" 
		self.restaurant_name=restaurant_name
		self.restaurant_type=restaurant_type
		self.restaurant_OC=restaurant_OC 
		self.client_serve = 0
	def get_descriptive_name(self):
		""" Imprime las caracteristicas en la pantalla""" 
		long_name = self.restaurant_name+' '+self.restaurant_type + ' '+self.restaurant_OC  
		return long_name.title()
	def read_number(sefl):
		"""Imprime los clientes qeu se han atendido"""
		print("se han atendido "+str(sefl.client_serve)+ " clientes.")
		 
my_new_restaurant=restaurant('Chiringuito','Mexicana','open') 
print(my_new_restaurant.get_descriptive_name()) 
my_new_restaurant.read_number()
