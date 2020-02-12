class user():
	def __init__(self,first_name,last_name,pasword,mail):
		self.first_name=first_name
		self.last_name=last_name
		self.pasword=pasword
		self.mail=mail
		self.user_attempt = 0
		self.reset=0
	def describe_user(self):
		print('\nName of user: '+self.first_name)
		print('\nlast name of user: '+self.last_name)
		print('\npasword: '+self.pasword)
		print('\nmail: '+self.mail)
	def greet_user(self):
		print('Hola, '+self.first_name+', welcome to the program.')
	def increment_login_attempts(self,us):
		if us <= 10:
			self.user_attempt = us
		else: print("you tried too many times to log in")
	def reset_loging_attempts(self):
	 	self.reset=user_attempt
	def read_number(sefl):
		"""Imprime los clientes qeu se han atendido"""
		print("se han intentado iniciar sesion "+str(sefl.user_attempt)+ " veces.")
my_user=user('Edwin','Gonzalez','Soporte321','edwingonzales@gmail.es')
print(my_user.describe_user())
my_user.increment_login_attempts(1)
my_user.read_number()
my_user.increment_login_attempts(2)
my_user.read_number()
my_user.increment_login_attempts(3)
my_user.read_number()
my_user.increment_login_attempts(4)
my_user.read_number()
my_user.increment_login_attempts(6)
my_user.read_number()
my_user.increment_login_attempts(7)
my_user.read_number()
my_user.increment_login_attempts(8)
my_user.read_number()
my_user.increment_login_attempts(9)
my_user.read_number()
my_user.increment_login_attempts(10)
my_user.read_number()
my_user.increment_login_attempts(11)
my_user.read_number()
my_user.increment_login_attempts(12)
my_user.read_number()